# RethinkDB: "TypeError: 'Var' object is not callable" when using lambda function in filter
r.db('my_db').table('my_table').filter(lambda row: row['some_key'].match(".sometext."))
