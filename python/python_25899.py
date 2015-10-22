# MongoDB update an array element matching a condition using $push
db.collection.update(
   {"charachters.char_name": "Testarion"},
   {"$push": {"charachters.$.parties": "party_user"}})
