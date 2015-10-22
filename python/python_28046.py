# Having Trouble with multiple "groupby" with a variable and a category (binned data)
#Depending on the content of vol_B you can do astype(int) or astype(float) as well.
gb = df.groupby([df['vol_B'].astype(str), df['expiry']])
