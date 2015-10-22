# how to set values to rows of boolean filtered dataframe column
data.loc[data["Brand"].isin(group_clients), "FreeSec"] = True
