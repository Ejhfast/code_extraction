# how to use aggregation in mongodb?
db.zips.aggregate([ {$group:{_id:{state:"$state"},numberOfzipcodes:{$sum:1}}}, {$sort:{numberOfzipcodes:-1}}, {$limit:4}])
