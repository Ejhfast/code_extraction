# Create stacked bar plot in pandas
out_dec_df.drop('country_name', axis=1).T.plot(kind='bar',stacked=True)
