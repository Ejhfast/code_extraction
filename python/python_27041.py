# Transforming a Dataframe for statsmodels t-test
ttest_ind(df[df['Treatment'] == 'a']['Performance'], df[df['Treatment'] == 'b']['Performance'])
