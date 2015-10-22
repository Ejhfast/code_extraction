# Overly complex expression to calculate the change in a Pandas series
&gt;&gt;&gt; df['Change'] = np.log(df['stat']).diff()
