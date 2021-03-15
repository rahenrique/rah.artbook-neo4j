import os
from flask import Flask
from neo4j import GraphDatabase

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

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

    @app.route("/")
    def hello():
        return "Hello, World!"

    # # register the database commands
    # from flaskr import db

    # db.init_app(app)

    # # apply the blueprints to the app
    # from flaskr import auth, blog

    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    # # make url_for('index') == url_for('blog.index')
    # # in another app, you might define a separate main index here with
    # # app.route, while giving the blog blueprint a url_prefix, but for
    # # the tutorial the blog will be the main index
    # app.add_url_rule("/", endpoint="index")


    uri = "bolt://n4j-db:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "test"))

    def create_person(tx, name):
        tx.run("CREATE (p:Person { name: $name }) ", name=name)

    def create_friend_of(tx, name, friend):
        tx.run("MATCH (a:Person) WHERE a.name = $name "
            "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
            name=name, friend=friend)

    # with driver.session() as session:
    #     session.write_transaction(create_person, "Alice")
    #     session.write_transaction(create_person, "Bob")
    #     session.write_transaction(create_person, "Carl")

    # with driver.session() as session:
    #     session.write_transaction(create_friend_of, "Alice", "Bob")
    #     session.write_transaction(create_friend_of, "Alice", "Carl")

    driver.close()


    return app
