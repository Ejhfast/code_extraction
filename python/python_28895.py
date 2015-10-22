# DateOffset from Year to Month and Week
range_max = df['recvd_dttm'].max()
range_min = range_max - (df['recvd_dttm']+pd.DateOffset(years=1))
