from flask import request
from flask_restx import Namespace, Resource

from artbook import db
from artbook.adapters.neo4j.repository import EventRepository
from artbook.domain.event import Event as ModelEvent


api = Namespace('events', description='Events related operations', path='/api/events')


@api.route('/<string:id>')
class Event(Resource):
    def get(self, id):
        database = db.get_db()
        repository = EventRepository(database)
        event = repository.get(id)

        if event:
            return event.serialize()

        abort(404, message="event '{}' not found".format(id))


@api.route('/')
class EventList(Resource):
    def get(self):
        database = db.get_db()
        repository = EventRepository(database)
        results = repository.all()

        return [event.serialize() for event in results]

    def post(self):
        data = request.get_json()
        title = data.get('title')
        start = data.get('start')
        end = data.get('end')

        if not title:
            return {'title': 'This field is required.'}, 400

        event = ModelEvent(title=title, start=start, end=end)
        database = db.get_db()
        repository = EventRepository(database)
        new = repository.add(event)

        return new, 201
