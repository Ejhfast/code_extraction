# how to add column name present in the list object into table
cursor.execute("create table " + config.table + " (" + ", ".join(config.cols) + ")")
