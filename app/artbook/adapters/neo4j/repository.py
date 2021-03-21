import uuid

from artbook.adapters.repository import AbstractRepository
from artbook.domain.models import Artist


class ArtistRepository(AbstractRepository):
    def add(self, artist:Artist) -> str:
        return self.db.read_transaction(self.__add_artist, artist)

    def get(self, id) -> Artist:
        result = self.db.read_transaction(self.__get_artist_by_id, id)
        if result:
            return Artist.hydrate(result)
        return None

    def all(self):
        results = self.db.read_transaction(self.__get_all_artists)
        return [Artist.hydrate(record) for record in results]


    @staticmethod
    def __add_artist(tx, artist):
        query = (
            '''
            CREATE (artist:Artist {id: $id, name: $name}) 
            RETURN artist
            '''
        )
        params = {
            'id': str(uuid.uuid4()),
            'name': artist.name
        }
        result = tx.run(query, params).single()

        if result and result.get('artist'):
            return result['artist']['id']
        return None 

    @staticmethod
    def __get_artist_by_id(tx, id):
        query = (
            '''
            MATCH (artist:Artist {id: $id}) 
            RETURN artist
            '''
        )
        result = tx.run(query, id=id).single()

        if result and result.get('artist'):
            return result['artist']
        return None 

    @staticmethod
    def __get_all_artists(tx):
        query = (
            '''
            MATCH (artist:Artist) 
            RETURN artist
            '''
        )
        results = list(tx.run(query))

        return [record['artist'] for record in results]
