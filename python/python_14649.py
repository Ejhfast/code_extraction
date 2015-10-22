# webapp2 user store, how do you query it
from webapp2_extras.appengine.auth.models import User
myusers = User.query().fetch()
