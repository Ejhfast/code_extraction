# Calculating Covariance in Pandas Time Series
df = pd.pivot_table(df, rows='WEEK_END_DATE', cols='TITLE_SHORT', values='SALES', aggfunc="sum")
