# Case insensitive pandas dataframe.merge
df_address['country_lower'] = df_address['Country'].str.lower()
df_CountryMapping['name_lower'] = df_CountryMapping['NAME'].str.lower()
df_merged = df_address.merge(df_CountryMapping, left_on="country_lower", right_on="name_lower", how="left")
