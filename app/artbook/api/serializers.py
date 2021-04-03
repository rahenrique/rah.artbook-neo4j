# TODO Fix bug preventing creation of Swagger JSON
from flask_restx import Api, Model, Resource, fields


artist = Model('Artist', {
    'id': fields.String(readOnly=True, description='The unique identifier of an artist', example='e0a08a2b-f415-48dd-8d30-c792949c3f5e'),
    'name': fields.String(example='Pablo Picasso'),
    'birth': fields.Date(example='1881-10-25'),
    'death': fields.Date(example='1973-04-08'),
    'alternative_names': fields.List(fields.String, example=['Pablo Ruiz Picasso','Picasso']),
})
