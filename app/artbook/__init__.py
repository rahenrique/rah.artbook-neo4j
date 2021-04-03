import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask

from artbook import db
from artbook.api.api import api


def create_app(test_config=None):

    load_dotenv(find_dotenv())

    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTX_MASK_SWAGGER'] = False
    
    api.init_app(app)
    db.init_app(app)

    return app
