from datetime import date


class Artwork():
    def __init__(self, title: str, creation: date, **params):
        self.__id = params.get('id')
        self.title = title
        self.creation = creation

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
            'creation': self.creation
        }


class ArtworkSeries():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name