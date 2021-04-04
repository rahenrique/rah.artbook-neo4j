import uuid

from artbook.adapters.repository import AbstractRepository
from artbook.domain.artist import Artist
from artbook.domain.artwork import Artwork
from artbook.domain.event import Event


class ArtistRepository(AbstractRepository):
    def add(self, artist:Artist) -> str:
        return self.db.read_transaction(self.__add_artist, artist)

    def get(self, uuid) -> Artist:
        result = self.db.read_transaction(self.__get_artist_by_id, uuid)
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
            CREATE (artist:Artist {uuid: $uuid, name: $name}) 
            RETURN artist
            '''
        )
        params = {
            'uuid': str(uuid.uuid4()),
            'name': artist.name
        }
        result = tx.run(query, params).single()

        if result and result.get('artist'):
            return result['artist']['uuid']
        return None

    @staticmethod
    def __get_artist_by_id(tx, uuid):
        query = (
            '''
            MATCH (artist:Artist {uuid: $uuid}) 
            RETURN artist
            '''
        )
        result = tx.run(query, uuid=str(uuid)).single()

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


class ArtworkRepository(AbstractRepository):
    def add(self, artwork:Artwork) -> str:
        return self.db.read_transaction(self.__add_artwork, artwork)

    def get(self, uuid) -> Artwork:
        result = self.db.read_transaction(self.__get_artwork_by_id, uuid)
        if result:
            return Artwork.hydrate(result)
        return None
    
    def all(self):
        results = self.db.read_transaction(self.__get_all_artworks)
        return [Artwork.hydrate(record) for record in results]

    def get_similar(self, uuid):
        results = self.db.read_transaction(self.__get_similar_artworks, uuid)
        return [Artwork.hydrate(record) for record in results]


    @staticmethod
    def __add_artwork(tx, artwork):
        query = (
            '''
            CREATE (artwork:Artwork {uuid: $uuid, title: $title, creation: $creation}) 
            RETURN artwork
            '''
        )
        params = {
            'uuid': str(uuid.uuid4()),
            'title': artwork.title,
            'creation': artwork.creation
        }
        result = tx.run(query, params).single()

        if result and result.get('artwork'):
            return result['artwork']['uuid']
        return None

    @staticmethod
    def __get_artwork_by_id(tx, uuid):
        query = (
            '''
            MATCH (artwork:Artwork {uuid: $uuid}) 
            OPTIONAL MATCH (artwork)-[:USES_TECHNIQUE]->(technique:Technique) 
            RETURN artwork{.*, techniques: COLLECT(DISTINCT technique.name)} 
            '''
        )
        result = tx.run(query, uuid=str(uuid)).single()

        if result and result.get('artwork'):
            return result['artwork']
        return None 

    @staticmethod
    def __get_all_artworks(tx):
        query = (
            '''
            MATCH (artwork:Artwork) 
            OPTIONAL MATCH (artwork)-[:USES_TECHNIQUE]->(technique:Technique) 
            RETURN artwork{.*, techniques: COLLECT(DISTINCT technique.name)}
            '''
        )
        results = list(tx.run(query))

        return [record['artwork'] for record in results]
    
    @staticmethod
    def __get_similar_artworks(tx, uuid):
        query = (
            '''
            MATCH (this:Artwork)-[:USES_TECHNIQUE]->(technique:Technique),
                (that:Artwork)-[:USES_TECHNIQUE]->(technique)
            WHERE this.uuid = {uuid} AND this <> that
            WITH that, COLLECT(DISTINCT technique.name) AS techniques
            ORDER BY SIZE(techniques) DESC LIMIT 25 
            MATCH (that:Artwork)-[:USES_TECHNIQUE]->(that_technique:Technique)  
            RETURN that{.*, techniques: COLLECT(DISTINCT that_technique.name)}
            '''
        )
        results = list(tx.run(query, uuid=str(uuid)))

        return [record['that'] for record in results]


class ArtworkAuthorshipRepository(AbstractRepository):
    def get_authors(self, artwork_id):
        results = self.db.read_transaction(self.__get_authors, artwork_id)
        return [Artist.hydrate(record) for record in results]

    def get_artworks(self, author_id):
        results = self.db.read_transaction(self.__get_artworks, author_id)
        return [Artwork.hydrate(record) for record in results]

    def add(self, artwork_id, artist_id):
        result = self.db.read_transaction(self.__add_authorship, artwork_id, artist_id)
        return result
    
    def get(self, reference):
        pass

    def all(self):
        pass


    @staticmethod
    def __get_authors(tx, artwork_id):
        query = (
            '''
            MATCH (author:Artist)-[:AUTHOR_OF]->(artwork:Artwork {uuid: $artwork_id}) 
            RETURN author
            '''
        )
        results = list(tx.run(query, artwork_id=str(artwork_id)))

        return [record['author'] for record in results]

    @staticmethod
    def __get_artworks(tx, author_id):
        query = (
            '''
            MATCH (author:Artist {uuid: $author_id})-[:AUTHOR_OF]->(artwork:Artwork) 
            OPTIONAL MATCH (artwork)-[:USES_TECHNIQUE]->(technique:Technique) 
            RETURN artwork{.*, techniques: COLLECT(DISTINCT technique.name)}
            '''
        )
        results = list(tx.run(query, author_id=str(author_id)))

        return [record['artwork'] for record in results]

    @staticmethod
    def __add_authorship(tx, artwork_id, artist_id):
        query = (
            '''
            MATCH (artist:Artist {uuid: $artist_id}) 
            MATCH (artwork:Artwork {uuid: $artwork_id}) 
            CREATE (artist)-[:AUTHOR_OF]->(artwork) 
            RETURN artwork, artist
            '''
        )
        params = {
            'artwork_id': str(artwork_id),
            'artist_id': str(artist_id)
        }
        result = tx.run(query, params)

        return [{"artwork": record["artwork"]["uuid"], "artist": record["artist"]["uuid"]} for record in result]


class EventRepository(AbstractRepository):
    def add(self, event:Event) -> str:
        return self.db.read_transaction(self.__add_event, event)

    def get(self, uuid) -> Event:
        result = self.db.read_transaction(self.__get_event_by_id, uuid)
        if result:
            return Event.hydrate(result)
        return None

    def update(self, uuid, event:Event) -> Event:
        result = self.db.read_transaction(self.__update_event_by_id, uuid, event)
        if result:
            return Event.hydrate(result)
        return None

    def patch(self, uuid, params:dict) -> Event:
        result = self.db.read_transaction(self.__patch_event_by_id, uuid, params)
        if result:
            return Event.hydrate(result)
        return None

    def delete(self, uuid) -> bool:
        result = self.db.read_transaction(self.__delete_event_by_id, uuid)
        return result
    
    def all(self):
        results = self.db.read_transaction(self.__get_all_events)
        return [Event.hydrate(record) for record in results]


    @staticmethod
    def __add_event(tx, event):
        query = (
            '''
            CREATE (event:Event {uuid: $uuid, title: $title, start: $start, end: $end}) 
            RETURN event
            '''
        )
        params = {
            'uuid': str(uuid.uuid4()),
            'title': event.title,
            'start': event.start,
            'end': event.end
        }
        result = tx.run(query, params).single()

        if result and result.get('event'):
            return result['event']['uuid']
        return None

    @staticmethod
    def __get_event_by_id(tx, uuid):
        query = (
            '''
            MATCH (event:Event {uuid: $uuid}) 
            RETURN event
            '''
        )
        result = tx.run(query, uuid=str(uuid)).single()

        if result and result.get('event'):
            return result['event']
        return None 

    @staticmethod
    def __update_event_by_id(tx, uuid, event):
        query = (
            '''
            MATCH (event:Event {uuid: $uuid}) 
            SET 
                event.title = {title}, 
                event.start = {start}, 
                event.end = {end} 
            RETURN event 
            '''
        )
        params = {
            'uuid': str(uuid),
            'title': event.title,
            'start': event.start,
            'end': event.end
        }

        result = tx.run(query, params).single()

        if result and result.get('event'):
            return result['event']
        return None 
    
    @staticmethod
    def __patch_event_by_id(tx, uuid, params):
        clauses = []
        for key in params:
            clauses.append('event.'+key+' = {'+key+'}')
        sets = 'SET '+','.join(clauses)

        query = "MATCH (event:Event {uuid: $uuid}) "+sets+" RETURN event"
        
        params["uuid"] = str(uuid)

        result = tx.run(query, params).single()

        if result and result.get('event'):
            return result['event']
        return None 

    @staticmethod
    def __delete_event_by_id(tx, uuid):
        query = (
            '''
            MATCH (event:Event {uuid: $uuid}) 
            DETACH DELETE event
            RETURN true as deleted
            '''
        )
        result = tx.run(query, uuid=str(uuid)).single()

        if result and result.get('deleted'):
            return result['deleted']
        return False 
    
    @staticmethod
    def __get_all_events(tx):
        query = (
            '''
            MATCH (event:Event) 
            RETURN event
            '''
        )
        results = list(tx.run(query))

        return [record['event'] for record in results]
