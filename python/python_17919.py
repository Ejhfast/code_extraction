# MySQL Python update rows
for k in range(city_count):
    cur.execute("UPDATE hqstock SET citylastprice = '%s' WHERE id = '%s'"% (CITYPRICE[k],   tID[k]))
    cur.commit()
