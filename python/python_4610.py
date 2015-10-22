# MySQL: Get column name or alias from query
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
