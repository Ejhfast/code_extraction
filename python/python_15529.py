# Checking if record exists in MongoDB
db.mycollection.ensureIndex({_id:1, date1:1, date2:1, number:1, type:1}, {unique: true});
