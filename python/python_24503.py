# Getting (index, column) pairs for True elements of a boolean DataFrame in Pandas
list(x[x &gt; 0].stack().index)
