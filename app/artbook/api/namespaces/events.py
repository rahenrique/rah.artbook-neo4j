from flask import request
from flask_restx import Namespace, Resource, abort

from artbook import db
from artbook.adapters.neo4j.repository import EventRepository
from artbook.domain.event import Event as ModelEvent

from artbook.api.parsers import event as eventParser
from artbook.api.parsers import partialEvent as partialEventParser
from artbook.api.serializers import event as eventSerializer


nsevents = Namespace('events', description='Events related operations', path='/api/events')
nsevents.models[eventSerializer.name] = eventSerializer


@nsevents.route('/<uuid:uuid>')
class Event(Resource):
    @nsevents.doc(params={'uuid': 'The unique identifier of the event.'})
    @nsevents.marshal_with(eventSerializer)
    def get(self, uuid):
        """
        Returns details about an event.
        """
        database = db.get_db()
        repository = EventRepository(database)
        event = repository.get(uuid)

        if event:
            return event

        abort(404, message="Event '{}' not found".format(uuid))
    

    @nsevents.response(400, 'Validation error')
    @nsevents.doc(params={'uuid': 'The unique identifier of the event.'})
    @nsevents.expect(eventParser)
    @nsevents.marshal_with(eventSerializer)
    def put(self, uuid):
        """
        Updates details about an event.
        """
        args = eventParser.parse_args(request)
        title = args.get('title')
        start = args.get('start')
        end = args.get('end')

        event = ModelEvent(uuid=uuid, title=title, start=start, end=end)
        database = db.get_db()
        repository = EventRepository(database)
        updated = repository.update(uuid, event)

        if updated:
            return updated

        abort(404, message="Event '{}' not found".format(uuid))


    @nsevents.response(400, 'Validation error')
    @nsevents.doc(params={'uuid': 'The unique identifier of the event.'})
    @nsevents.expect(partialEventParser)
    @nsevents.marshal_with(eventSerializer)
    def patch(self, uuid):
        """
        Partially updates details about an event.
        """
        args = partialEventParser.parse_args(request)
        # title = args.get('title')
        # start = args.get('start')
        # end = args.get('end')

        params = {k: v for k, v in args.items() if v is not None}
        # params["uuid"] = uuid
    
        # event = ModelEvent(uuid=uuid, title=title, start=start, end=end)
        # event = ModelEvent(**params)
        database = db.get_db()
        repository = EventRepository(database)
        updated = repository.patch(uuid, params)

        if updated:
            return updated

        abort(404, message="Event '{}' not found".format(uuid))


    @nsevents.response(204, 'Event successfully deleted')
    @nsevents.response(400, 'Validation error')
    @nsevents.doc(params={'uuid': 'The unique identifier of the event.'})
    def delete(self, uuid):
        """
        Deletes an event
        """
        database = db.get_db()
        repository = EventRepository(database)
        success = repository.delete(uuid)

        return None, 204



@nsevents.route('/')
class EventCollection(Resource):
    @nsevents.marshal_with(eventSerializer, as_list=True)
    def get(self):
        """
        Returns list of events.
        """
        database = db.get_db()
        repository = EventRepository(database)
        results = repository.all()

        return [event for event in results]


    @nsevents.response(201, 'Event successfully created', eventSerializer)
    @nsevents.response(400, 'Validation error')
    @nsevents.expect(eventParser)
    def post(self):
        """
        Creates a new event.
        """
        args = eventParser.parse_args(request)
        uuid = args.get('uuid')
        title = args.get('title')
        start = args.get('start')
        end = args.get('end')

        event = ModelEvent(uuid=uuid, title=title, start=start, end=end)
        database = db.get_db()
        repository = EventRepository(database)
        new = repository.add(event)

        return new, 201
