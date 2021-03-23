from datetime import date
from artbook.domain.models import Technique


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
