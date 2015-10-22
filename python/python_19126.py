# OperationalError: near "if": syntax error
cursor.execute("insert or replace into items values(:id,:img,:def,:name)",{"id":itemid,"def":item['defindex'],"img": item['image_url_large'],"name": item['name']})
