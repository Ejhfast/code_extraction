# Python: Cancel object creation during initialization
data = [good, bad]
theList = [obj for obj in (MyObject(some_data) for some_data in data) if obj.data_is_valid]
