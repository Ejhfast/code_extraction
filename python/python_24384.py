# Pandas dataframe from generator where each line is a tab-separated row
pd.DataFrame([x.split('\t') for x in test])
