# adding column to dataframe based on count from another dataframe
ranksdf["t_wins"]  = ranksdf.apply(lambda x: len(matchesdf[(matchesdf['t_date'] &lt; x['date']) &amp; (matchesdf['w_name'] == x['player']) &amp; (matchesdf['round'] == 'F')]), axis =1)
