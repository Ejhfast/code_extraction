# Getting SQLAlchemy to issue CREATE SCHEMA on create_all
from sqlalchemy.schema import CreateSchema
engine.execute(CreateSchema('my_schema'))
