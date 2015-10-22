# How to use map() to convert (key,values) pair to values only in Pyspark
wordCounts
.map(lambda x:x[1])
.reduce(lambda x,y:x + y)
