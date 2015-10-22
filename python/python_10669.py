# Retrieving only the most recent row in MySQL
SELECT *
FROM yourtable
WHERE date_and_time = (SELECT MAX(date_and_time) FROM yourtable)
