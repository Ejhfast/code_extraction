# Google appengine datastore tree structure
class Node(db.Model):
    children = db.ListProperty(db.Key)
