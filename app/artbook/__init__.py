import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify
from neo4j import GraphDatabase, basic_auth

from artbook import model


def create_app(test_config=None):

    load_dotenv(find_dotenv())

    app = Flask(__name__, instance_relative_config=True)

    # def output_json(data, code, headers=None):
    #     return json_response(data_=data, headers_=headers, status_=code)

    DATABASE_USERNAME = os.getenv('MOVIE_DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('MOVIE_DATABASE_PASSWORD')
    DATABASE_URL = os.getenv('MOVIE_DATABASE_URL')

    driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(DATABASE_USERNAME, str(DATABASE_PASSWORD)))

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    @app.route("/")
    def hello():
        return "Hello, ArtBook"
    
    artists = [
        {
            'id': 1,
            'name': u'Pablo Picasso',
            'alternative_names': {
                u'Ruiz Blasco Picasso y Lopez',
                u'Pablo Ruiz y Picasso
                u'Pablo Ruiz Blasco',
                u'Pablo Diego José Francisco de Paula Juan Nepomuceno Crispín Crispiniano de la Santissima Trinidad Ruiz Blasco Picasso',
                u'Pablo Ruiz Picasso' 
            },
            'birth_date': '1881-10-25',
            'death_date': '1973-04-08' 
        },
        {
            'id': 2,
            'name': u'Claude Monet',
            'alternative_names': {
                u'Claude Oscar Monet',
                u'Claude Jean Monet',
                u'Claude-Oscar Monet',
                u'Oscar Claude Monet',
                u'Oscar-Claude Monet'
            },
            'birth_date': '1840-11-14',
            'death_date': '1926-12-05'
        }
    ]

    @app.route('/api/v1.0/artists', methods=['GET'])
    def get_artists():
        return jsonify({'artists': artists})


    driver.close()

    return app
