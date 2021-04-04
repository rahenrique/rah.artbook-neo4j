from flask_restx import Api, Model, Resource, fields


artist = Model('Artist', {
    'uuid': fields.String(readOnly=True, description='The unique identifier of the artist.', example='e0a08a2b-f415-48dd-8d30-c792949c3f5e'),
    'name': fields.String(description='Preferable name (or nickname) the artist is known by.', example='Pablo Picasso'),
    'birth': fields.Date(description='The date of birth of the artist.', example='1881-10-25'),
    'death': fields.Date(description='The date of death of the artist.', example='1973-04-08'),
    'alternative_names': fields.List(fields.String(), description='Another names the artist is known by.', example=['Pablo Ruiz Picasso','Picasso']),
})


artwork = Model('Artwork', {
    'uuid': fields.String(readOnly=True, description='The unique identifier of the artwork.', example='9e6e1552-72e1-4deb-b60e-a8b5ceb23ddd'),
    'title': fields.String(description='Title of the artwork.', example='Guernica'),
    'creation': fields.Date(description='The date of creation of the artwork.', example='1937'),
    'techniques': fields.List(fields.String(), description='Techniques used in the artwork.', example=['Pintura','Óleo sobre tela']),
})


event = Model('Event', {
    'uuid': fields.String(readOnly=True, description='The unique identifier of the event.', example='2639dc5a-b5c5-4525-86b1-5486545bfee4'),
    'title': fields.String(description='Name or title of the event.', example='Exposição 2018'),
    'start': fields.Date(description='Start date of the event.', example='2018-01-01'),
    'end': fields.Date(description='End date of the event.', example='2018-06-01'),
})
