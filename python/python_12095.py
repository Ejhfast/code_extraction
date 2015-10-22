# psycopg - INSERT gzipped data into bytea column
cur.execute("INSERT INTO public.test VALUES (%s)", (psycopg2.Binary(data),))
