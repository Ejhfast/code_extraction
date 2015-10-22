# Print different precision by column with pandas.DataFrame.to_csv()?
df_data['vals'] = df_data['vals'].map(lambda x: '%2.1f' % x)
