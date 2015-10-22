# Applying a python function that returns a list and writing to columns of dataframe
df_new.apply(lambda r: pd.Series(function_taking_row(r), index=colnames), axis=1)
