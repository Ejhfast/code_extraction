# How do I convert a numpy array into a pandas dataframe?
px2 = px.reshape((-1,3))
df = pd.DataFrame({'R':px2[:,0],'G':px2[:,1],'B':px2[:,2]})
