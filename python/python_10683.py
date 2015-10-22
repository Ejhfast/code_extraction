# Python get micro time from certain date
def microtime(dt):
    time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0
