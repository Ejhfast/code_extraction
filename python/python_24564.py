# Which function in spark is used to combine two RDDs by keys
(rdd1 union rdd2).reduceByKey(_ ++ _)
