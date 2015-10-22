# equivalent connection for postgres and sqlite
conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
conn = psycopg2.connect(conn_string)
