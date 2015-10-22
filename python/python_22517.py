# PySpark Drop Rows
val header = data.first
val rows = data.filter(line =&gt; line != header)
