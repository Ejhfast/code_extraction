# Python: double Backslash formatting
file_path = r"d:\folder\file.csv"
cursor.execute("LOAD data local INFILE %s INTO TABLE test ...);", file_path)
