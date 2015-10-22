# django transaction.commit_manually leads to 'MySQL server has gone away'
from django import db
db.close_connection()
