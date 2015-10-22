# How can I extend Python's datetime.datetime with my own methods?
import datetime
def millisecond(dt):
    return dt.microsecond/1000
