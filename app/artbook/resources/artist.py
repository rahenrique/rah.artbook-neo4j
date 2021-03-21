import uuid
from flask import Flask, abort, g, jsonify, make_response, redirect
from flask_restful import Resource, request

# from artbook.domain.model import Artist
from artbook.service.neo4j.repository import ArtistRepository


class Artist(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self, id):
        repository = ArtistRepository(self.db)
        artist = repository.get(id)

        if artist:
            return artist.serialize()
        
        abort(404, message="artist {} not found".format(id))


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

        results = self.db.write_transaction(create_artist, name)
        artist = results['artist']
        return artist, 201
