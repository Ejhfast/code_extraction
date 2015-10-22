# Define Pandas DataFrame as composite boolean condition
data['thing'] = (data['a'] &gt; 0.75) &amp; (data['b'] &gt; 0.5)
