# Dropping rows from a Dataframe based on Date
df['dt']=pandas.Datetimeindex(df['maturity_dt'])
newdf=df.loc[df['dt']&lt;=todays_date].copy()
