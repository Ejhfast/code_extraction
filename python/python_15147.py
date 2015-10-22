# Trouble escaping mysql statement in python
cursor.execute("SELECT MIN(id) FROM title WHERE provider=%s"
               "AND vendor_id LIKE '%s%%'", (provider, vendor_id_stem))
