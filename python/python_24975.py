# python mapreduce job returning error
hduser@bharti-desktop:~/hadoop$ bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -input /user/hduser/gutenberg/gutenberg/ -output /user/hduser/op4 -mapper /home/hduser/hadoop/mapper1.py -file /home/hduser/hadoop/mapper1.py -reducer /home/hduser/hadoop/reducer1.py -file /home/hduser/hadoop/reducer1.py
