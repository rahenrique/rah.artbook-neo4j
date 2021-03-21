from flask import Flask
from flask_restful import Resource, abort, request, fields, marshal_with

from artbook.domain.model import Artist as ModelArtist
from artbook.infra.neo4j.repository import ArtistRepository


class Artist(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self, id):
        repository = ArtistRepository(self.db)
        artist = repository.get(id)

        if artist:
            return artist.serialize()
        
        abort(404, message="artist '{}' not found".format(id))


class ArtistList(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

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
