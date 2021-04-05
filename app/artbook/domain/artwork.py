from datetime import date

from artbook.services.services import Neo4JDate
from .technique import Technique


class Artwork():
    def __init__(self, **params):
        self.__uuid = params.get('uuid')
        self.title = params.get('title')
        self.creation = params.get('creation')
        self.__techniques = set()

    def __repr__(self):
        return "%s - %s" % (self.title, self.creation.isoformat())
    
    @staticmethod
    def hydrate(data):
        artwork = Artwork(
            uuid = data['uuid'],
            title = data['title'],
            creation = Neo4JDate.toDate(data['creation']),
        )
        if data['techniques']:
            artwork.add_techniques(data['techniques'])
        return artwork

    @property
    def uuid(self):
        return self.__uuid

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
