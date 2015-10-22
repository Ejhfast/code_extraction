# Using MySQL functions in python
sql = """INSERT INTO RawData(DateTime) VALUES (STR_TO_DATE(%s, '%%d/%%b/%%Y:%%T'))"""% (date_time)
