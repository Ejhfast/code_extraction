# Django / MySql not honouring unique_together
db.create_index('row_locks', ['table_name','locked_row_id'], unique=True)
