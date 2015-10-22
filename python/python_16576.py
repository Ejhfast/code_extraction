# Python - how can i read in and read out so that other readers can read it for further pursing?
$ java -cp /var/tmp/Audio.jar Main.Boot | tee /var/tmp/log.log | python -u /var/tmp/consumer.py &amp;
$ tail -f /var/tmp/log.log
