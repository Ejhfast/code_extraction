# Passing a column name as a variable to a select statement in a function in python / pandas
querysting = "select Year, {} from table where Year={}".format(c,y)
df = pd.read_sql(querystring,db)
