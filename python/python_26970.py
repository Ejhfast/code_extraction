# Filtering Pandas Dataframe using OR statement
alldata_balance = alldata[(alldata[IBRD] !=0) | (alldata[IMF] !=0)]
