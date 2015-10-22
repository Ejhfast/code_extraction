# How to insert map type into cassandra using cassandra-driver for python
cql = "Insert into table_name (my_key, name, my_dict) values (%s, %s, %s)"
session.execute(cql,  (my_key, name, my_dict))
