# takeOrdered key error with Pyspark in Python 3
sc.parallelize([("a", 10), ("c", 5), ("b", 7)]).takeOrdered(3, key=lambda kv: -kv[1])
