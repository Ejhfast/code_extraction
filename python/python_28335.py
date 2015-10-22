# what is the best method to extract highly correlated vaiables within the given threshold
corr_val=0.01
df2 = df1.corr().unstack().reset_index()
df2[df2[0]&gt;corr_val]
