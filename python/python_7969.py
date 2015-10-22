# How to get entity by child id while child is already deleted?
k = db.Key.from_path(FbUser.kind(), 131)
room = Room.all().filter('fb_user =', k).get()
db.delete(room)
