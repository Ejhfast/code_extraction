# Finding the last values before a specific value in numpy/pandas
s = pd.Series([9, 0, 3, 0, 1, 9, 4, 9, 0, 0, 9, 4, 0]) #using your example array
s = s[s.isin([0,9])]
s[(s == 0) &amp; (s.shift(-1) == 9)]
