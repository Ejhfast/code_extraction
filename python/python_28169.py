# RethinkDB chaining/combining filters
r.db('items').table('tokens')
 .filter(r.row('valid_to').gt(r.now()))
 .filter(r.row["processed"] == False)
