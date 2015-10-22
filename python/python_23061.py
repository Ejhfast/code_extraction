# SQL python concatenation error
table_sql = """CREATE TABLE %s (gid integer NOT NULL DEFAULT nextval('%s'),point_x numeric,point_y numeric,value double precision,name varchar(50),geom geometry(Point, %%s),CONSTRAINT %s PRIMARY KEY(gid))""" % (name_table, name_seq, name_pkey)
