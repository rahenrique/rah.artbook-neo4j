from flask import request
from flask_restx import Namespace, Resource, abort

from artbook import db
from artbook.adapters.neo4j.repository import ArtistRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork

from artbook.api.parsers import artist as artistParser
from artbook.api.serializers import artist as artistSerializer
from artbook.api.serializers import artwork as artworkSerializer


nsartists = Namespace('artists', description='Artists related operations', path='/api/artists')
nsartists.models[artistSerializer.name] = artistSerializer
nsartists.models[artworkSerializer.name] = artworkSerializer


@nsartists.route('/<uuid:uuid>')
class Artist(Resource):
    @nsartists.doc(params={'uuid': 'The unique identifier of the artist.'})
    @nsartists.marshal_with(artistSerializer)
    def get(self, uuid):
        """
        Returns details about an artist.
        """
        database = db.get_db()
        repository = ArtistRepository(database)
        artist = repository.get(uuid)

        if artist:
            return artist
        
        abort(404, message="Artist '{}' not found".format(uuid))


    @nsartists.response(400, 'Validation error')
    @nsartists.doc(params={'uuid': 'The unique identifier of the artist.'})
    @nsartists.expect(artistParser)
    @nsartists.marshal_with(artistSerializer)
    def put(self, uuid):
        """
        Updates details about an artist.
        """
        args = artistParser.parse_args(request)
        name = args.get('name')
        birth = args.get('birth')
        death = args.get('death')
        alternative_names = args.get('alternative_names')

        artist = ModelArtist(name=name, birth=birth, death=death, alternative_names=alternative_names)
        
        database = db.get_db()
        repository = ArtistRepository(database)
        updated = repository.update(uuid, artist)

        if updated:
            return updated

        abort(404, message="Artist '{}' not found".format(uuid))

@nsartists.route('/')
class ArtistCollection(Resource):
    @nsartists.marshal_with(artistSerializer, as_list=True)
    def get(self):
        """
        Returns list of artists.
        """
        database = db.get_db()
        repository = ArtistRepository(database)
        results = repository.all()
        return [artist for artist in results]


    @nsartists.response(201, 'Artist successfully created', artistSerializer)
    @nsartists.response(400, 'Validation error')
    @nsartists.expect(artistParser)
    def post(self):
        """
        Creates a new artist.
        """
        args = artistParser.parse_args(request)
        name = args.get('name')
        birth = args.get('birth')
        death = args.get('death')
        alternative_names = args.get('alternative_names')

        artist = ModelArtist(name=name, birth=birth, death=death, alternative_names=alternative_names)
        
        database = db.get_db()
        repository = ArtistRepository(database)
        new = repository.add(artist)

        return new, 201



@nsartists.route('/<uuid:uuid>/artworks/')
class ArtistAuthorship(Resource):
    @nsartists.doc(params={'uuid': 'The unique identifier of the artist.'})
    @nsartists.marshal_with(artworkSerializer, as_list=True)
    def get(self, uuid):
        """
        Returns a list of an artist's artworks (authorship).
        """
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_artworks(uuid)

        return [artwork for artwork in results]
