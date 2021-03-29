from flask_restx import Api

from .artists import api as nsartists
from .artworks import api as nsartworks
from .events import api as nsevents

api = Api(
    title='ArtBook API',
    version='1.0',
    description='Catálogo de artes e artistas',
)

api.add_namespace(nsartists)
api.add_namespace(nsartworks)
api.add_namespace(nsevents)
