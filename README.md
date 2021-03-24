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

Run unit tests

```
$ docker-compose run --rm api ./manage.py test
```

## Deploy

```
// ssh onto the node /srv/trippy
// deploy new task & api containers from GCR (TODO: look into getting docker compose installed & auth'd properly to pull from GCR)
// maybe redis or nginx if needed
// instructions TBD
$ docker-compose up # start server
```

## Development

### Adding new dependencies

```
pipenv install <package>
# pin package, update requirements.txt
# rebuild containers
DOCKER_BUILDKIT=1 docker build --rm -t gcr.io/joshpaulchan/trippy-api:latest . # build image
```

### Adding new configuration

1. Add new variable(s) to `<app>/apps.py` config class.
2. Set it there (w or without a default) (can import from environment)
3. Import it in your applications and use it however you want.
