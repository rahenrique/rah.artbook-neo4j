ArtBook
=======

Art catalog in Python, using Flask and Neo4J.

This is a personal project, mainly focused on learning technologies, aiming to build an API for a catalog of arts and artists, on the Flask Framework, with persistence in a Neo4J graph database. The application structure seeks an approach that adheres to the concepts of Domain Driven Design, with a hexagonal architecture.

**Work In Progress - It documents a learning process**

## Starting

### Prerequisites

Before starting, you will need to have the following tools installed on your machine:
* [Git](https://git-scm.com)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation (Local Development)

```bash
# Clone this repository
$ git clone https://github.com/rahenrique/artbook-neo4j.git

# Run the application in development mode using the embedded server
$ make init

# If necessary, edit the .env file (based on the .env.example file)
$ nano app/.env
```

The Flask server will start on port:5000 in development mode. Any source code changes will automatically reflect in the running application.

Acess:
* API Docs (Swagger): <http://0.0.0.0:5000/>
* App: <http://0.0.0.0:5000/api/artists/>
* Neo4jBrowser: <http://localhost:7474/browser/>

Optionally, it is possible to run the application using Gunicorn. Just force the use of docker-compose.yml file without overrides

```bash
$ docker-compose -f docker-compose.yml up -d
```
The Gunicorn server will start at port:8080. In this way, the application ***will not automatically reload*** after source code changes.
Acess:
* App: <http://localhost:8080/api/artists/>

## Running tests

To run the initial seed of the database, use the following command:
```bash
$ make db-seed
```

To run the tests, from your terminal (on your local machine), run the following command:

```bash
$ make test
```

Other useful commands during development can be consulted using:

```bash
$ make help
```

## Built With

* [Flask](https://flask.palletsprojects.com/)
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/stable/index.html)
* [Neo4j](https://neo4j.com/)
* [nginx](https://nginx.org/en/)
