from flask import request
from flask_restx import Namespace, Resource, abort

from artbook import db
from artbook.adapters.neo4j.repository import ArtworkRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork

from artbook.api.parsers import artwork as artworkParser
from artbook.api.serializers import artist as artistSerializer
from artbook.api.serializers import artwork as artworkSerializer


nsartworks = Namespace('artworks', description='Artwork related operations', path='/api/artworks')
nsartworks.models[artistSerializer.name] = artistSerializer
nsartworks.models[artworkSerializer.name] = artworkSerializer


@nsartworks.route('/<uuid:uuid>')
class Artwork(Resource):
    @nsartworks.doc(params={'uuid': 'The unique identifier of the artwork.'})
    @nsartworks.marshal_with(artworkSerializer)
    def get(self, uuid):
        """
        Returns details about an artwork.
        """
        database = db.get_db()
        repository = ArtworkRepository(database)
        artwork = repository.get(uuid)

        if artwork:
            return artwork
        
        abort(404, message="Artwork '{}' not found".format(uuid))



@nsartworks.route('/')
class ArtworkCollection(Resource):
    @nsartworks.marshal_with(artworkSerializer, as_list=True)
    def get(self):
        """
        Returns list of artworks.
        """
        database = db.get_db()
        repository = ArtworkRepository(database)
        results = repository.all()
        return [artwork for artwork in results]


    @nsartworks.response(201, 'Artwork successfully created', artworkSerializer)
    @nsartworks.response(400, 'Validation error')
    @nsartworks.expect(artworkParser)
    def post(self):
        """
        Creates a new artwork.
        """
        args = artworkParser.parse_args(request)
        title = args.get('title')
        creation = args.get('creation')
        techniques = args.get('techniques')

        database = db.get_db()
        artwork = ModelArtwork(title=title, creation=creation, techniques=techniques)
        repository = ArtworkRepository(database)
        new = repository.add(artwork)

        return new, 201



@nsartworks.route('/<uuid:uuid>/similar/')
class ArtworkSimilarityCollection(Resource):
    @nsartworks.doc(params={'uuid': 'The unique identifier of the artwork.'})
    @nsartworks.marshal_with(artworkSerializer, as_list=True)
    def get(self, uuid):
        """
        Returns list of similar artworks, based on techniques.
        """
        database = db.get_db()
        repository = ArtworkRepository(database)
        results = repository.get_similar(uuid)

        return [artwork for artwork in results]



@nsartworks.route('/<uuid:uuid>/authors/')
class ArtworkAuthorship(Resource):
    @nsartworks.doc(params={'uuid': 'The unique identifier of the artwork.'})
    @nsartworks.marshal_with(artistSerializer, as_list=True)
    def get(self, uuid):
        """
        Returns a list of an artworks' artists (authorship).
        """
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_authors(uuid)

        return [artist for artist in results]

    
    @nsartworks.doc(params={'uuid': 'The unique identifier of the artwork.'})
    @nsartworks.param('author', description='The unique identifier of the artist.', required=True)
    def post(self, uuid):
        """
        Creates an authorship relationship to an artwork.
        """
        data = request.get_json()
        author = data.get('author')

        if not author:
            return {'author': 'This field is required. '}, 400
        
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        authorship = repository.add(uuid, author)
        
        return authorship, 201
