# How to specify psycopg2 parameter for an array for timestamps (datetimes)
SELECT somestuff
FROM mytable
WHERE thetimestamp = ANY (%(times)s::timestamp[])
