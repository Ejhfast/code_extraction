# RethinkDB-DB not found
r.db_create("authors").run()
r.db("authors").table_create("books").run()
r.db("authors").table("books").count()
