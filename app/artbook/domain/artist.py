from datetime import date
from artbook.services.services import Neo4JDate


class Artist():
    def __init__(self, **params):
        self.__uuid = params.get('uuid')
        self.name = params.get('name')
        self.birth = params.get('birth')
        self.death = params.get('death')
        self.__alternative_names = params.get('alternative_names', set())

    def __repr__(self):
        return self.name
    
    @staticmethod
    def hydrate(data):
        return Artist(
            uuid = data['uuid'],
            name = data['name'],
            birth = Neo4JDate.toDate(data['birth']),
            death = Neo4JDate.toDate(data['death']),
            alternative_names = set() if data['alternative_names'] is None else data['alternative_names']
        )

    @property
    def uuid(self):
        return self.__uuid

    @property
    def alternative_names(self):
        return self.__alternative_names

    def add_alternative_names(self, *alternative_names):
        for altname in alternative_names:
            self.__alternative_names.add(altname)

    def remove_alternative_names(self, *alternative_names):
        for altname in alternative_names:
            self.__alternative_names.discard(altname)
