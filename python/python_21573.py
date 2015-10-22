# NDB Query: reverse relationships of ndb.KeyProperty
def getWhoFollowsMe(me_key):
  return User.query().filter(User.follows==me_key)
