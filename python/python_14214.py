# Running the Python Code on Hadoop Failed
hduser@ubuntu:/usr/local/hadoop$ bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/reducer.py -reducer /home/hduser/reducer.py -input /user/hduser/gutenberg/* -output /user/hduser/gutenberg-output
