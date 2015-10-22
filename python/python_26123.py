# Pandas combine row element in one
df= pd.DataFrame(np.random.randn(10,4))
df[4]= [[df[2][x],df[3][x]] for x in range(df.shape[0])]
