# Python: Start psql query, don't wait for response
conn = psycopg2.connect(database='mydb', async=1)
