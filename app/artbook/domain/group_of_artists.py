from datetime import date


class GroupOfArtists():
    def __init__(self, name: str, foundation: date=None, end: date=None):
        self.name = name
        self.foundation = foundation
        self.end = end

    def __repr__(self):
        return self.name