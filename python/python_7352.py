# Using OR in SQLAlchemy
from sqlalchemy import or_
filter(or_(User.name == 'ed', User.name == 'wendy'))
