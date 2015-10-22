# Quicker way of updating subdocuments
db.stuff.ensureIndex( { "i.elements.timestamp" : 1 });
