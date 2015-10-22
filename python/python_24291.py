# Python pandas: Setting row values in Pandas using data of that column
t = np.random.normal(size=100)
t[0] = vol
df = pd.DataFrame(t.cumsum())
