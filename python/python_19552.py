# Apply formula to specific numpy array values
cond2 = (SPN &gt;= -alpha) &amp; (SPN &lt;= 0)
SPN[cond2] = -np.cos(SPN[cond2]*np.pi/(2*alpha))
