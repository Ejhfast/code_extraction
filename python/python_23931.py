# Pandas Python: sort df while excluding given rows by label
excluded = df_raw[~df_raw.index.isin(exclude_list)]
