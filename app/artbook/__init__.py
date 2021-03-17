import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, abort, g, jsonify, make_response, redirect
from flask_restful import Api, Resource
from neo4j import GraphDatabase, basic_auth

from .model import Artist, ArtistList


def create_app(test_config=None):

    load_dotenv(find_dotenv())

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    # def output_json(data, code, headers=None):
    #     return json_response(data_=data, headers_=headers, status_=code)

    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_URL = os.getenv('DATABASE_URL')

    driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(DATABASE_USERNAME, str(DATABASE_PASSWORD)))

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    api.add_resource(ArtistList, '/api/artists/')
    api.add_resource(Artist, '/api/artists/<int:artist_id>')
    
    # def get_db():
    #     if not hasattr(g, 'neo4j_db'):
    #         g.neo4j_db = driver.session()
    #     return g.neo4j_db


    # @app.teardown_appcontext
    # def close_db(error):
    #     if hasattr(g, 'neo4j_db'):
    #         g.neo4j_db.close()
    
    
    # @app.route('/')
    # def index():
    #     return redirect('/api/artists/')

    # @app.route('/api/artists/', methods=['GET'])
    # def get_artists():
    #     return jsonify(artists)

    # @app.route('/api/artists/<int:artist_id>', methods=['GET'])
    # def get_artist(artist_id):
    #     artist = [artist for artist in artists if artist['id'] == artist_id]
    #     if len(artist) == 0:
    #         abort(404)
    #     return jsonify(artist[0])

    # @app.errorhandler(404)
    # def not_found(error):
    #     return make_response(jsonify({'error': 'Not found'}), 404)



    # if __name__ == '__main__':
    #     app.run(debug=True)

    return app
