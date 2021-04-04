from flask import request
from flask_restx import Namespace, Resource

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


@nsartworks.route('/<uuid:id>')
class Artwork(Resource):
    @nsartworks.param('id', description='The unique identifier of the artwork.', required=True)
    @nsartworks.marshal_with(artworkSerializer)
    def get(self, id):
        """
        Returns details about an artwork.
        """
        database = db.get_db()
        repository = ArtworkRepository(database)
        artwork = repository.get(id)

        if artwork:
            return artwork
        
        abort(404, message="Artwork '{}' not found".format(id))



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



@nsartworks.route('/<uuid:id>/similar/')
class ArtworkSimilarityCollection(Resource):
    @nsartworks.param('id', description='The unique identifier of the artwork.', required=True)
    @nsartworks.marshal_with(artworkSerializer, as_list=True)
    def get(self, id):
        """
        Returns list of similar artworks, based on techniques.
        """
        database = db.get_db()
        repository = ArtworkRepository(database)
        results = repository.get_similar(id)

        return [artwork for artwork in results]



@nsartworks.route('/<uuid:id>/authors/')
class ArtworkAuthorship(Resource):
    @nsartworks.param('id', description='The unique identifier of the artwork.', required=True)
    @nsartworks.marshal_with(artistSerializer, as_list=True)
    def get(self, id):
        """
        Returns a list of an artworks' artists (authorship).
        """
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_authors(id)

        return [artist for artist in results]


    @nsartworks.param('id', description='The unique identifier of the artwork.', required=True)
    @nsartworks.param('author', description='The unique identifier of the artist.', required=True)
    def post(self, id):
        """
        Creates an authorship relationship to an artwork.
        """
        data = request.get_json()
        author = data.get('author')

        if not author:
            return {'author': 'This field is required. '}, 400
        
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        authorship = repository.add(id, author)
        
        return authorship, 201
