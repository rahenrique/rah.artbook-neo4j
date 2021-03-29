from flask import request
from flask_restx import Namespace, Resource

from artbook import db
from artbook.adapters.neo4j.repository import ArtworkRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork


api = Namespace('artworks', description='Artwork related operations', path='/api/artworks')


@api.route('/<string:id>')
class Artwork(Resource):
    def get(self, id):
        database = db.get_db()
        repository = ArtworkRepository(database)
        artwork = repository.get(id)

        if artwork:
            return artwork.serialize()
        
        abort(404, message="artwork '{}' not found".format(id))


@api.route('/')
class ArtworkList(Resource):
    def get(self):
        database = db.get_db()
        repository = ArtworkRepository(database)
        results = repository.all()
        return [artwork.serialize() for artwork in results]

    def post(self):
        data = request.get_json()
        title = data.get('title')
        creation = data.get('creation')

        if not title:
            return {'title': 'This field is required.'}, 400
        
        if not creation:
            return {'creation': 'This field is required.'}, 400

        database = db.get_db()
        artwork = ModelArtwork(title=title, creation=creation)
        repository = ArtworkRepository(database)
        new = repository.add(artwork)

        return new, 201


@api.route('/<string:id>/similar/')
class ArtworkSimilarityList(Resource):
    def get(self, id):
        database = db.get_db()
        repository = ArtworkRepository(database)
        results = repository.get_similar(id)

        return [artwork.serialize() for artwork in results]


@api.route('/<string:id>/authors/')
class ArtworkAuthorship(Resource):
    def get(self, id):
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        results = repository.get_authors(id)

        return [artist.serialize() for artist in results]

    def post(self, id):
        data = request.get_json()
        author = data.get('author')

        if not author:
            return {'author': 'This field is required. '}, 400
        
        database = db.get_db()
        repository = ArtworkAuthorshipRepository(database)
        authorship = repository.add(id, author)
        
        return authorship, 201
