# How to find matching rows in Pandas DataFrame with identical values with same/opposite signs in certain columns?
ndf = merge(left=df1,right=df1,on=('c','d'),how='inner')
out = ndf[(ndf.a_x == (-1)*ndf.a_y) &amp; (ndf.b_x == (-1)*ndf.b_y)]
