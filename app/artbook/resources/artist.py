from flask import Flask, g
from flask_restful import Resource


def serialize_artist(artist):
    return {
        'id': artist['id'],
        'name': artist['name']
    }


class Artist(Resource):

    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self, id):
        def get_artist_by_id(tx, id):
            return tx.run(
                '''
                MATCH (artist:Artist {id: $id}) RETURN artist 
                ''', {'id': id}
            ).single()

        result = self.db.read_transaction(get_artist_by_id, id)
        
        if result and result.get('artist'):
            return serialize_artist(result["artist"])
        
        abort(404, message="The requested Artist #({}) doesn't exist".format(id))


class ArtistList(Resource):

    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self):
        def get_artist_list(tx):
            return list(tx.run(
                '''
                MATCH (artist:Artist) RETURN artist
                '''
            ))
        
        results = self.db.read_transaction(get_artist_list)
        return [serialize_artist(record['artist']) for record in results]
        
    def post(self):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {'name': 'This field is required.'}, 400

        def create_artist(tx, name):
            return tx.run(
                '''
                CREATE (artist:Artist {id: $id, name: $name}) RETURN artist
                ''',
                {
                    'id': str(uuid.uuid4()),
                    'name': name
                }
            ).single()

        results = self.db.write_transaction(create_artist, name)
        artist = results['artist']
        return artist, 201