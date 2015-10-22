# get the count and group them
db.collection.aggregate({$group:{_id:"$loc", count: {$sum:1}}}
