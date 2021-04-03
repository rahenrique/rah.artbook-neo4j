from flask import request
from flask_restx import Api, Model, Namespace, Resource, abort

from artbook import db
from artbook.adapters.neo4j.repository import ArtistRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork
from artbook.api.parsers import artist as artistParser
from artbook.api.serializers import artist as artistSerializer


nsartists = Namespace('artists', description='Artists related operations', path='/api/artists')
nsartists.models[artistSerializer.name] = artistSerializer


@nsartists.route('/<uuid:id>')
class Artist(Resource):
    @nsartists.doc(params={'id': 'The unique identifier of an artist'})
    @nsartists.marshal_with(artistSerializer)
    def get(self, id):
        """
        Returns details about an artist.
        """
        database = db.get_db()
        repository = ArtistRepository(database)
        artist = repository.get(id)

        if artist:
            return artist #.serialize()
        
        abort(404, message="Artist '{}' not found".format(id))


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
        return [artist for artist in results] #.serialize()

    @nsartists.response(201, 'Artist successfully created', artistSerializer)
    @nsartists.response(400, 'Validation error')
    # @nsartists.expect(artistParser)
    # @nsartists.doc(params={'name': 'Preferable name (or nickname) the artist is known by'})
    def post(self):
        """
        Creates a new artist.
        """
        args = artistParser.parse_args(request)
        name = args.get('name')

        database = db.get_db()
        artist = ModelArtist(name=name)
        repository = ArtistRepository(database)
        new = repository.add(artist)

        return new, 201


@nsartists.route('/<uuid:id>/artworks/')
class ArtistAuthorship(Resource):
    @nsartists.doc(params={'id': 'The unique identifier of an artist'})
    def get(self, id):
        """
        Returns a list of an artist's artworks (authorship).
        """
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_artworks(id)

        return [artwork.serialize() for artwork in results]