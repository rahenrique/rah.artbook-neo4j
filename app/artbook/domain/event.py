from datetime import date


class Event():
    def __init__(self, **params):
        self.__id = params.get('id')
        self.title = title
        self.start = start
        self.end = end

    def __repr__(self):
        return "%s (%s- %s)" % (self.title, self.start.isoformat(), self.end.isoformat())
    
    @staticmethod
    def hydrate(data):
        return Artwork(
            id = data['id'],
            title = data['title'],
            start = data['start'],
            end = data['end']
        )
    
    def serialize(self):
        return {
            'id': self.__id,
            'title': self.title,
            'start': self.start,
            'end': self.end
        }
