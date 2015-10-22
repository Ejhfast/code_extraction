# Format pandas datatime object to show fiscal years from Feb to Feb and be formatted as %Y?
df['DATE']=pd.to_datetime(df.DATE).apply(pd.Period, freq='A-FEB')
