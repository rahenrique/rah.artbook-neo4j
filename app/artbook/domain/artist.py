from datetime import date


class Artist():
    def __init__(self, **params):
        self.__id = params.get('id')
        self.name = params.get('name')
        self.birth = params.get('birth')
        self.death = params.get('death')
        self.__alternative_names = {}

    def __repr__(self):
        return self.name
    
    @staticmethod
    def hydrate(data):
        return Artist(
            id = data['id'],
            name = data['name']
        )
    
    def serialize(self):
        return {
            'id': self.__id,
            'name': self.name,
            'birth': self.birth,
            'death': self.death,
            'alternative_names': list(self.__alternative_names)
        }
    
    @property
    def id(self):
        return self.__id
    
    @property
    def alternative_names(self):
        return self.__alternative_names
    
    def add_alternative_names(self, *alternative_names):
        for altname in alternative_names:
            self.__alternative_names.add(altname)
    
    def remove_alternative_names(self, *alternative_names):
        for altname in alternative_names:
            self.__alternative_names.discard(altname)

