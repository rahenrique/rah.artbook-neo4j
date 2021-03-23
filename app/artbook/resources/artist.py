from flask import Flask
from flask_restful import Resource, abort, request, fields, marshal_with

from artbook.adapters.neo4j.repository import ArtistRepository, ArtworkRepository, ArtworkAuthorshipRepository
from artbook.domain.artist import Artist as ModelArtist
from artbook.domain.artwork import Artwork as ModelArtwork


class BaseResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']


class Artist(BaseResource):
    def get(self, id):
        repository = ArtistRepository(self.db)
        artist = repository.get(id)

        if artist:
            return artist.serialize()
        
        abort(404, message="artist '{}' not found".format(id))


class ArtistList(BaseResource):
    def get(self):
        repository = ArtistRepository(self.db)
        results = repository.all()

        return [artist.serialize() for artist in results]

    def post(self):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {'name': 'This field is required.'}, 400

        artist = ModelArtist(name=name)
        repository = ArtistRepository(self.db)
        new = repository.add(artist)

        return new, 201


class Artwork(BaseResource):
    def get(self, id):
        repository = ArtworkRepository(self.db)
        artwork = repository.get(id)

        if artwork:
            return artwork.serialize()
        
        abort(404, message="artwork '{}' not found".format(id))


class ArtworkList(BaseResource):
    def get(self):
        repository = ArtworkRepository(self.db)
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

        artwork = ModelArtwork(title=title, creation=creation)
        repository = ArtworkRepository(self.db)
        new = repository.add(artwork)

        return new, 201


class ArtworkAuthorship(BaseResource):
    def get(self, id):
        repository = ArtworkAuthorshipRepository(self.db)
        results = repository.get_authors(id)

        return [artist.serialize() for artist in results]

    def post(self, id):
        data = request.get_json()
        author = data.get('author')

        if not author:
            return {'author': 'This field is required. '}, 400
        
        repository = ArtworkAuthorshipRepository(self.db)
        authorship = repository.add(id, author)
        
        return authorship, 201

class ArtistAuthorship(BaseResource):
    def get(self, id):
        repository = ArtworkAuthorshipRepository(self.db)
        results = repository.get_artworks(id)

        return [artwork.serialize() for artwork in results]
