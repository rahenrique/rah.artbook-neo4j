from flask_restx import Api

from .namespaces.artists import nsartists
from .namespaces.artworks import nsartworks
from .namespaces.events import nsevents


api = Api(
    title='ArtBook API',
    version='1.0',
    description='Catálogo de artes e artistas em Python, utilizando Flask e Neo4J. \n\nEste é um projeto pessoal, focado principalmente no aprendizado de tecnologias, visando construir uma API de um catálogo de artes e artistas, sobre o Framework Flask, com persistência em um banco de dados grafo Neo4J. A estrutura da aplicação busca uma abordagem que seja aderente aos conceitos de Domain Driven Design, com uma arquitetura hexagonal.',
)


api.add_namespace(nsartists)
api.add_namespace(nsartworks)
api.add_namespace(nsevents)
