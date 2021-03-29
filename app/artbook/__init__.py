import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask

from artbook import db
from artbook.apis import api


def create_app(test_config=None):

    load_dotenv(find_dotenv())

    app = Flask(__name__, instance_relative_config=True)
    api.init_app(app)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # a simple page that says hello
    @app.route('/api/')
    def hello():
        return {"message":"Hello, World!"}


    db.init_app(app)

    return app
