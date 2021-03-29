from flask import request
from flask_restx import Namespace, Resource

from artbook import db
from artbook.adapters.neo4j.repository import ArtistRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork


api = Namespace('artists', description='Artists related operations', path='/api/artists')


@api.route('/<uuid:id>')
@api.doc(params={'id': 'UUID for an Artist'})
class Artist(Resource):
    def get(self, id):
        database = db.get_db()
        repository = ArtistRepository(database)
        artist = repository.get(id)

        if artist:
            return artist.serialize()
        
        abort(404, message="artist '{}' not found".format(id))


@api.route('/')
class ArtistList(Resource):
    def get(self):
        database = db.get_db()
        repository = ArtistRepository(database)
        results = repository.all()
        return [artist.serialize() for artist in results]

    def post(self):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {'name': 'This field is required.'}, 400

        database = db.get_db()
        artist = ModelArtist(name=name)
        repository = ArtistRepository(database)
        new = repository.add(artist)

        return new, 201


@api.route('/<uuid:id>/artworks/')
class ArtistAuthorship(Resource):
    def get(self, id):
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_artworks(id)

        return [artwork.serialize() for artwork in results]
