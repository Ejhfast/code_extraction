# Dealing with data from MySQL using Python
import pandas
cur = db.cursor()
nf = pandas.io.sql.read_frame("select * from tablename limit 50;", db)
