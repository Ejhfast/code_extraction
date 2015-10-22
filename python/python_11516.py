# Inserting json in Mysql from python json dump
value = '''{"cpa_type": "null", "...0:1347548413"}'''
  cursor.execute("INSERT INTO mytable (campaign_object) VALUES (%s)", (value,))
