# SparkSQL: HQL script in file to be loaded on Python code
count = sqlContext.sql(open("file.hql").read()).count()
