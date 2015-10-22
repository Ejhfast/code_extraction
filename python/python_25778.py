# How to load directory of JSON files into Apache Spark in Python
my_RDD_strings = sc.textFile(path_to_dir_with_JSON_files)
my_RDD_dictionaries = my_RDD_strings.map(json.loads)
