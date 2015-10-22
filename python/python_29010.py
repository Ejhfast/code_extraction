# java.util.HashMap missing in PySpark session
df.write.jdbc("jdbc:sqlserver://serverURL", "dbName.SparkTestTable1", "overwrite", dict(driver="com.microsoft.sqlserver.jdbc.SQLServerDriver", user="userName", password="password"))
