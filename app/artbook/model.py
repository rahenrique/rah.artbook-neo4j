from flask_restful import Api, Resource, abort

artists = [
    {
        'id': 1,
        'name': u'Pablo Picasso',
        'alternative_names': [
            u'Ruiz Blasco Picasso y Lopez',
            u'Pablo Ruiz y Picasso',
            u'Pablo Ruiz Blasco',
            u'Pablo Diego José Francisco de Paula Juan Nepomuceno Crispín Crispiniano de la Santissima Trinidad Ruiz Blasco Picasso',
            u'Pablo Ruiz Picasso' 
        ],
        'birth_date': '1881-10-25',
        'death_date': '1973-04-08' 
    },
    {
        'id': 2,
        'name': u'Claude Monet',
        'alternative_names': [
            u'Claude Oscar Monet',
            u'Claude Jean Monet',
            u'Claude-Oscar Monet',
            u'Oscar Claude Monet',
            u'Oscar-Claude Monet'
        ],
        'birth_date': '1840-11-14',
        'death_date': '1926-12-05'
    }
]

class Artist(Resource):

    def get(self, artist_id):
        artist = [artist for artist in artists if artist['id'] == artist_id]
        if len(artist) == 0:
            abort(404, message="The requested Artist #({}) doesn't exist".format(artist_id))
        return artist

class ArtistList(Resource):
    
    def get(self):
        return artists
    
    # def get(self):
    #     def get_artists(tx):
    #         return list(tx.run('MATCH (genre:Genre) SET genre.id=id(genre) RETURN genre'))
    #     db = get_db()
    #     result = db.read_transaction(get_genres)
    #     return [serialize_genre(record['genre']) for record in result]
