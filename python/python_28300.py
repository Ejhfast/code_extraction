# Replacing NaT with Epoch in Pandas
data[col_name] = a_col.apply(lambda x: x if isinstance(x, datetime.datetime)
                                       and not isinstance(x, pd.tslib.NaTType) else epoch)
