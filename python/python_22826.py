# Pandas dataframe merge and element-wide multiplication
cols = [each for each in df2.columns if each not in ['name','bin']]
df3 = pd.merge(df1, df2, how='left', on=['bin'])
df3[cols] = df3.apply(lambda x:x['score']*x[cols],axis=1)
