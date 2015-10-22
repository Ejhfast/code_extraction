# Regular expressions in PySpark textFile command
glob = "/home/spark-1.4.0/A/B_2{0}/Output/CSV.csv".format("[0-9]" * 8)
lines = sc.textFile(glob)
