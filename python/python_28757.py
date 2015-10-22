# DBF - encoding cp1250
import dbf
with dbf.Table('test.dbf') as table:
    dbf.export(table, 'junk.csv')
