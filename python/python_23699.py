# Error while testing postgresql database with python
curs.execute("SELECT exists(SELECT 1 from pg_catalog.pg_database where datname = %s)", ('mydb',))
