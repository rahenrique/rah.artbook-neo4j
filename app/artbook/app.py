import os
import uuid

from dotenv import load_dotenv, find_dotenv
from neo4j import GraphDatabase, basic_auth
from flask import Flask, g
from flask_restful import Api

from artbook.resources.artist import Artist, Artwork, ArtistList, ArtworkList, ArtworkAuthorship, ArtistAuthorship, Event, EventList



def create_app(test_config=None):

    load_dotenv(find_dotenv())

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_URL = os.getenv('DATABASE_URL')

    driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(DATABASE_USERNAME, str(DATABASE_PASSWORD)))

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)


    def get_db():
        if not hasattr(g, 'neo4j_db'):
            g.neo4j_db = driver.session()
        return g.neo4j_db

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'neo4j_db'):
            g.neo4j_db.close()


    with app.app_context():
        db = get_db()


    api.add_resource(ArtistList, '/api/artists/', resource_class_kwargs={'db': db})
    api.add_resource(Artist, '/api/artists/<string:id>', resource_class_kwargs={'db': db})

    api.add_resource(ArtworkList, '/api/artworks/', resource_class_kwargs={'db': db})
    api.add_resource(Artwork, '/api/artworks/<string:id>', resource_class_kwargs={'db': db})

    api.add_resource(ArtworkAuthorship, '/api/artworks/<string:id>/authors/', resource_class_kwargs={'db': db})
    api.add_resource(ArtistAuthorship, '/api/artists/<string:id>/artworks/', resource_class_kwargs={'db': db})

    api.add_resource(EventList, '/api/events/', resource_class_kwargs={'db': db})
    api.add_resource(Event, '/api/events/<string:id>', resource_class_kwargs={'db': db})


    return app