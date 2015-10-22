# create temporary table from cursor
sql.execute(connection, """
INSERT INTO blah VALUES %s;""" % (
    ", ".join("(%d)" % hid for hid in hids)))
