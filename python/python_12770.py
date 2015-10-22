# Passing table name as a parameter in psycopg2
SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' and table_name=%s LIMIT 1
