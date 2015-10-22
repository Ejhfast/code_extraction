# Updating a new key in an embedded document
db.stuff.update({'id':i['id'], 'counts.name':element['name']}, {'$set': {'counts.$.newfield':total}})
