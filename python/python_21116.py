# python inserting into mysql
sql = u'INSERT INTO RegionName (Name, Perent, X1, X2, Z1, Z2) VALUES ("%s","%s",%d,%d,%d,%d)'% (Name, Perent, x1, x2, z1, z2)
    cur.execute(sql)
