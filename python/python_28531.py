# Migrating database from local development to Heroku-Django 1.8
pg_dump --no-acl --no-owner -h localhost -U myuser myd | heroku pg:psql
