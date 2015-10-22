# Clean way of creating list of hours
import datetime as dt
hours = [(i, dt.time(i).strftime('%I %p')) for i in range(24)]
