# Calculating time difference of each occurance of a IP
df['tvalue'] = df.index
    df['delta'] = (df['tvalue']-df['tvalue'].shift()).fillna(0)
    df[(df.IP == '61.245.172.48')][['delta']]
