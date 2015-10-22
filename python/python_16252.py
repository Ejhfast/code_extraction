# Mongodb python syntax to get array value .
db.testpymongo.find(  { "Project": { $elemMatch: { "pname": "project1"  } } } )
