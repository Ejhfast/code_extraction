# Why does this code return a list index error?
result = [entry for entry in result if entry[0] &gt;= 0 and
  entry[0] &lt; board.dimensions and entry[1] &gt;= 0 and
  entry[1] &lt; board.dimensions]
