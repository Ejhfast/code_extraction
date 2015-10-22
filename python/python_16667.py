# Change Column Name
conn.cursor().execute("{call sp_rename(?,?,?)}",('xro_zips_import.CityAliasName', 'City', 'COLUMN'))
conn.commit()
