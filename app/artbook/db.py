import os

from dotenv import load_dotenv, find_dotenv
from neo4j import GraphDatabase, basic_auth
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if not hasattr(g, 'db'):
        load_dotenv(find_dotenv())

        DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        DATABASE_URL = os.getenv('DATABASE_URL')

        driver = GraphDatabase.driver(DATABASE_URL, auth=basic_auth(DATABASE_USERNAME, str(DATABASE_PASSWORD)))

        g.db = driver.session()
    return g.db

def close_db(error=None):
    if hasattr(g, 'db'):
        g.db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
