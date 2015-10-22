# How to modify a column present in a mysql database through python?
for row in rows:
        sub=re.sub(r'^[^,]*,', '', row[0])
        cursor.execute("UPDATE drug_specifications SET  categories=%s where id=%s;",(sub, str(row[0])))
