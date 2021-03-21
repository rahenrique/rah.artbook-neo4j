from datetime import date


class Artist():
    def __init__(self, **params):
        self.id = params.get('id')
        self.name = params.get('name')
        self.birth = params.get('birth')
        self.death = params.get('death')

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
            'id': self.id,
            'name': self.name,
            'birth': self.birth,
            'death': self.death
        }
    
    def addAltName(self, *altnames):
        for altname in altnames:
            self.altname = altname


class GroupOfArtists():
    def __init__(self, name: str, foundation: date=None, end: date=None):
        self.name = name
        self.foundation = foundation
        self.end = end

    def __repr__(self):
        return self.name


class Technique():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class ArtworkSeries():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class Artwork():
    def __init__(self, title: str, creation: date, technique: Technique=None):
        self.title = title
        self.creation = creation
        self.technique = technique

    def __repr__(self):
        return "%s - %s" % (self.title, self.creation.isoformat())