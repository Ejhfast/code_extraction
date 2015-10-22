# add multiple columns to an sqlite database in python
for i in listOfVars:
    cur.execute('''ALTER TABLE testTable ADD COLUMN %s TEXT''' % i)
