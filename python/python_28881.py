# Deleting Dataframe rows dynamically
df['dt']=pandas.Datetimeindex(df['maturity_dt'])
df=df.set_index('dt')
df=df.loc[(df.index.month==2) | (df.index.month==8)].copy()
