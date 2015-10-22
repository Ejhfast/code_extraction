# Keep finite entries only in Pandas
with pd.option_context('mode.use_inf_as_null', True):
   df = df.dropna()
