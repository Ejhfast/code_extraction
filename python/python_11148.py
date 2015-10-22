# Get Key in property List using GQL
recs = db.GqlQuery('select content from FileHistory')
for rec in recs:
  print rec.key(), rec.content
