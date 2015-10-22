# pandas if conditions met assign values to two variables
df = pd.DataFrame(np.random.randint(0, 10, size=(10, 4)), columns=list("ABCD"))
df.ix[(df.A &gt; 5) &amp; (df.B &lt; 8), ["A", "B"]] = -10, -10
