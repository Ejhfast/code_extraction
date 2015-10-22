# Managing dependencies with Hadoop Streaming?
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-0.17.0-streaming.jar -mapper mapper.py -reducer reducer.py -input input/foo -output output -file /tmp/foo.py -file /tmp/lib.zip
