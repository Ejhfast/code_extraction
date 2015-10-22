# python cursor FROM %s
cur.execute("""SELECT MAX(id) FROM %s WHERE equipement_id = %s""" % (table, eq_id))
