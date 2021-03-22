from datetime import date


class Artist():
    def __init__(self, **params):
        self.__id = params.get('id')
        self.name = params.get('name')
        self.birth = params.get('birth')
        self.death = params.get('death')
        self.__altnames = None

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
            'death': self.death
        }
    
    def addAltName(self, *altnames):
        for altname in altnames:
            self.__altnames = altname

    @property
    def id(self):
        return self.__id

class GroupOfArtists():
    def __init__(self, name: str, foundation: date=None, end: date=None):
        self.name = name
        self.foundation = foundation
        self.end = end

    def __repr__(self):
        return self.name


class Technique():
    def __init__(self, name: str):
        self.__name = name

    def __repr__(self):
        return self.__name


class ArtworkSeries():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Artwork():
    def __init__(self, title: str, creation: date, technique: Technique=None, **params):
        self.__id = params.get('id')
        self.title = title
        self.creation = creation
        self.technique = technique

    def __repr__(self):
        return "%s - %s" % (self.title, self.creation.isoformat())
    
    @staticmethod
    def hydrate(data):
        return Artwork(
            id = data['id'],
            title = data['title'],
            creation = data['creation']
        )
    
    def serialize(self):
        return {
            'id': self.__id,
            'title': self.title,
            'creation': self.creation,
            'technique': self.technique
        }