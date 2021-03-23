import abc


class AbstractRepository(abc.ABC):
    def __init__(self, db):
        self.db = db

    @abc.abstractmethod
    def add(self, batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abc.abstractmethod
    def all(self):
        raise NotImplementedError
