# python %s format specifier failing for utf-8 values
cursor.execute(u"INSERT INTO "+ unicode(DATA_TABLE) + u""" (fk_id, title, streetaddress,json)
                 values (%(fk_id)s, %(title)s, %(address)s, %(json)s ) """ ,(
                 result))
