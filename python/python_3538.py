# How to connect to a database through a Paramiko Tunnel (or similar package)
conn = psycopg2.connect(database="test", host="localhost", port=&lt;forward_port&gt;)
