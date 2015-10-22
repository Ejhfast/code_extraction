# Loading JSON dataset into Spark, then use filter, map, etc
import json
f = sc.textFile('/path/to/file')
d = lines.map(lambda line: json.loads(line))
