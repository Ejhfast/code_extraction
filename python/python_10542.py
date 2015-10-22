# Google App Engine GQL query on localhost
from google.appengine.ext import db
q = db.GqlQuery("SELECT * FROM Song WHERE composer = 'Lennon, John'")
