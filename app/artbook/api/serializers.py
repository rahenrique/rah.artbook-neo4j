from flask_restx import Api, Model, Resource, fields


artist = Model('Artist', {
    'id': fields.String(readOnly=True, description='The unique identifier of the artist.', example='e0a08a2b-f415-48dd-8d30-c792949c3f5e'),
    'name': fields.String(description='Preferable name (or nickname) the artist is known by.', example='Pablo Picasso'),
    'birth': fields.Date(description='The date of birth of the artist.', example='1881-10-25'),
    'death': fields.Date(description='The date of death of the artist.', example='1973-04-08'),
    'alternative_names': fields.List(fields.String(), description='Another names the artist is known by.', example=['Pablo Ruiz Picasso','Picasso']),
})


artwork = Model('Artwork', {
    'id': fields.String(readOnly=True, description='The unique identifier of the artwork.', example='9e6e1552-72e1-4deb-b60e-a8b5ceb23ddd'),
    'title': fields.String(description='Title of the artwork.', example='Guernica'),
    'creation': fields.Date(description='The date of creation of the artwork.', example='1937'),
    'techniques': fields.List(fields.String(), description='Techniques used in the artwork.', example=['Pintura','Óleo sobre tela']),
})
