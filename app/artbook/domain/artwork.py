from datetime import date

from .technique import Technique


class Artwork():
    def __init__(self, title: str, creation: date, **params):
        self.__id = params.get('id')
        self.title = title
        self.creation = creation
        self.__techniques = set()

    def __repr__(self):
        return "%s - %s" % (self.title, self.creation.isoformat())
    
    @staticmethod
    def hydrate(data):
        artwork = Artwork(
            id = data['id'],
            title = data['title'],
            creation = data['creation']
        )
        if data['techniques']:
            artwork.add_techniques(data['techniques'])
        return artwork
    
    # def serialize(self):
    #     return {
    #         'id': self.__id,
    #         'title': self.title,
    #         'creation': self.creation,
    #         'techniques': list(self.__techniques)
    #     }

    @property
    def id(self):
        return self.__id

    @property
    def techniques(self):
        return self.__techniques

    def add_techniques(self, *techniques):
        for technique in techniques:
            for t in technique:
                self.__techniques.add(t)

    def remove_techniques(self, *techniques):
        for technique in techniques:
            self.__techniques.discard(technique)
