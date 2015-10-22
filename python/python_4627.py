# How to rewrite deprecated DDL() statement in SQLAlchemy 0.7+
event.listen(child_table, "after-create", DDL(inherit).execute_if(dialect='postgresql'))
