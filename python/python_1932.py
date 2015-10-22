# Python appengine Query does not work when using a variable
def getItem(item_id):
    q = Item.all()
    q.filter("itemid = ", int(item_id))
