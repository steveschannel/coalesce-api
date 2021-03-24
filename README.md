# Getting Started

This is a "donation network" that runs on docker/django/graphene/postgres+gis extensions.

## Usage

### Running locally via docker

You can bring the applications up in background mode using:

```
$ docker-compose up -d # start server in detached (background mode)
```

### Common Commands

Restart api or celery jobs to take in your changes:

```
$ docker-compose restart api
```

Make migrations

```
$ docker-compose run --rm api ./manage.py makemigrations --noinput # setup the database
```

Run Migrations

```
$ docker-compose run --rm api ./manage.py migrate --noinput # setup the database
```

Load some fixtures for testing.

```
$ docker-compose run --rm api ./manage.py loaddata --app plan plan/fixtures/* # optional: load fixtures for development setup the database
```
