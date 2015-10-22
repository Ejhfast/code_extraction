# Hadoop Streaming Job failed error in python
hadoop@ubuntu:/usr/local/hadoop$ bin/hadoop jar contrib/streaming/hadoop-0.20.0-streaming.jar -file /home/hadoop/mapper.py -mapper mapper.py -file /home/hadoop/reducer.py -reducer reducer.py -input my-input/* -output my-output
