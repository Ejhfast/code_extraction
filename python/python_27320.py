# Cron job is writing the error to error log but fails to write outputs to output log file
31 10  * * 1-5 cd /home/alpha/IBpy &amp;&amp; stdbuf -i0 -o0 -e0 python ShortData.py &gt;&gt; /home/alpha/logs/Shortdata.op 2&gt;&gt; /home/alpha/logs/Shortdata.er
