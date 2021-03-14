from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello Python, Flask and Neo4J!'