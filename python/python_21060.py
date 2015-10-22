# Dataframe creation with weekdays or adding week days
df  = pd.DataFrame({'value' : [0,0,0,0,0,0,0,0,0,0]}, index=pd.date_range(pd.datetime(2014,3,30), freq='B', periods=10))
