# What is the best way to extract load average float values from a string in Python?
# s is the string to parse
loadavg = [float(x) for x in s.rsplit('load average: ', 1)[1].split(', ')]
