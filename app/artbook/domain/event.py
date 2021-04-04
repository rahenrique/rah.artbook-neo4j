from datetime import date, datetime
from artbook.services.services import Neo4JDate


class Event():
    def __init__(self, **params):
        self.__uuid = params.get('uuid')
        self.title = params.get('title')
        self.start = params.get('start')
        self.end = params.get('end')

    def __repr__(self):
        return "%s" % (self.title)
    
    @staticmethod
    def hydrate(data):
        return Event(
            uuid = data['uuid'],
            title = data['title'],
            start = Neo4JDate.toDate(data['start']),
            end = Neo4JDate.toDate(data['end']),
        )

    @property
    def uuid(self):
        return self.__uuid
