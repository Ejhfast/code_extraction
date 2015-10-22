# Hadoop streaming with multiple python files
hadoop jar $streamingJar -D mapreduce.map.memory.mb=4096 -files python_files
-input $input -output $output -mapper "python_files\python parse.py" -reducer NONE
