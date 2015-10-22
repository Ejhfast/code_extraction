# How to convert datetime to timestamp Python
def time_difference(datetime_time):
    delta = datetime.now() - datetime_time
    return int(delta.total_seconds())
