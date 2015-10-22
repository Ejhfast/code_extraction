# Modify data in pandas
condition = (df.ID=='a1') &amp; (df.geo=='DE')
df.ix[condition, 'value'] = 9999
