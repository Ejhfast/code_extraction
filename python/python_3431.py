# Psycopg2 using wildcard causes TypeError
SELECT * FROM events WHERE summary ILIKE E'%%test%%' AND start_time &gt; %(begin)s
