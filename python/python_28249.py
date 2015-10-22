# Pandas date time formatting with timezone shifting
df['time'] = pd.to_datetime(df['time'], unit='s')
df = df.set_index('time').tz_localize('US/Eastern').tz_convert('UTC').tz_convert(None).reset_index()
df['time'] = df['time'].dt.date
