ArtBook
=======

Catálogo de artes e artistas em Python, utilizando Flask e Neo4J. 

Este é um projeto pessoal, focado principalmente no aprendizado de tecnologias, visando construir uma API de um catálogo de artes e artistas, sobre o Framework Flask, com persistência em um banco de dados grafo Neo4J. A estrutura da aplicação busca uma abordagem que seja aderente aos conceitos de Domain Driven Design, com uma arquitetura hexagonal.

**Este é um Work In Progress, apresentado com todas as suas falhas inerentes ao processo de aprendizagem!** :blush:

## Iniciando

// TO-DO

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
* [Git](https://git-scm.com)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação (Desenvolvimento Local)

```bash
# Clone este repositório
$ git clone https://github.com/rahenrique/artbook-neo4j.git

# Execute a aplicação em modo de desenvolvimento, utilizando o servidor embarcado
$ docker-compose up -d
```

```bash
# Opcionalmente, é possível executar a aplicação utilizando Gunicorn
# Basta forçar o uso do arquivo docker-compose.yml sem overrides
$ docker-compose -f docker-compose.yml up -d
```

O servidor Flask inciará na porta:5000 em modo de desenvolvimento. Qualquer alteração de código-fonte irá refletir automaticamente na aplicação em execução.

Acesso:
* App: <http://0.0.0.0:5000/>
* Neo4jBrowser: <http://localhost:7474/browser/>

## Executando testes

// TO-DO

## Deployment

// TO-DO

## Built With

* [Flask](https://flask.palletsprojects.com/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/)
* [Neo4j](https://neo4j.com/)
* [nginx](https://nginx.org/en/)