# python-rrdtool, how to create graphs in UTC time zone
import time, os
os.environ['TZ'] = "Asia/Kolkata"   # timezone you want to display graphs in
time.tzset()
