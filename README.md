ArtBook
=======

Catálogo de artes e artistas em Python, utilizando Flask e Neo4J. 

Este é um projeto pessoal, focado principalmente no aprendizado de tecnologias, visando construir uma API de um catálogo de artes e artistas, sobre o Framework Flask, com persistência em um banco de dados grafo Neo4J. A estrutura da aplicação busca uma abordagem que seja aderente aos conceitos de Domain Driven Design, com uma arquitetura hexagonal.

**Work In Progress - representa um processo de aprendizagem!**

## Iniciando

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
$ make init

# Se necessário, edite o arquivo .env (baseado no arquivo .env.example)
$ nano app/.env
```

O servidor Flask inciará na porta:5000 em modo de desenvolvimento. Qualquer alteração de código-fonte irá refletir automaticamente na aplicação em execução.

Acesso:
* API Docs (Swagger): <http://0.0.0.0:5000/>
* App: <http://0.0.0.0:5000/api/artists/>
* Neo4jBrowser: <http://localhost:7474/browser/>

Opcionalmente, é possível executar a aplicação utilizando Gunicorn. Basta forçar o uso do arquivo docker-compose.yml sem overrides

```bash
$ docker-compose -f docker-compose.yml up -d
```
O servidor Gunicorn iniciará na porta:8080. Nesta forma, não acontecerá o reload automático da aplicação após alteraçes de código-fonte.
Acesso:
* App: <http://localhost:8080/api/artists/>

## Executando testes

Para fazer o seed inicial do banco de dados, rode o seguinte comando:
```bash
$ make db-seed
```

Para executar os testes, a partir do seu terminal (em sua máquina local), rode o seguinte comando:

```bash
$ make test
```

Demais comandos úteis durante o desenvolvimento, podem ser consultados pelo comando:

```bash
$ make help
```

## Deployment

// TO-DO

## Built With

* [Flask](https://flask.palletsprojects.com/)
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/stable/index.html)
* [Neo4j](https://neo4j.com/)
* [nginx](https://nginx.org/en/)
