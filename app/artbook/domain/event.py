from datetime import date


class Event():
    def __init__(self, **params):
        self.__id = params.get('id')
        self.title = params.get('title')
        self.start = params.get('start')
        self.end = params.get('end')

    def __repr__(self):
        return "%s (%s- %s)" % (self.title, self.start.isoformat(), self.end.isoformat())
    
    @staticmethod
    def hydrate(data):
        return Event(
            id = data['id'],
            title = data['title'],
            start = data['start'],
            end = data['end']
        )
