# Mysql timestamp Data truncated for column
cursor.execute("""INSERT INTO temps VALUES (%s,%s,CURRENT_TIMESTAMP)""",(avgtemperatures[0],avgtemperatures[1]))
