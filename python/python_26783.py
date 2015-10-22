# Proper way to convert bytea from Postgres back to a string in python
SELECT encode(some_hash, 'hex'), * FROM some_table WHERE some_hash in decode(another_hash, 'hex')
