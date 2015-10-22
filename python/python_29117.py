# Python and psycopg2 - convert python list of jsonb elements to postgres jsonb array
INSERT INTO my_table (data) VALUES (%s::jsonb[]);
