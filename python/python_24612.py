# Pandas: Select rows where a number of strings appear more than once
vehicles = {'ford', 'honda', 'toyota', 'steve_urkel_car'} #etc
df[df.isin(vehicles).sum(1) &gt;= 2]
