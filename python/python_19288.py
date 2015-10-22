# Pandas: getting the name of the minimum column
incomplete_df['reason'] = "Reason is " + incomplete_df.T.idxmin()
