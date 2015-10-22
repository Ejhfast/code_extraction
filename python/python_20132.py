# In Python entering variables(dates) from raw_input into postgreSQL SELECT...WHERE
query = "SELECT to_char(gltx.post_date, 'YYYYMMDD') FROM gltx WHERE (gltx.post_date &gt; %s AND gltx.post_date &lt; %s)"
args = (start_date, end_date)
cursor.execute(query, args)
