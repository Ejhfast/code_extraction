# Time to decimal time in Python
t = "1:12:23"
(h, m, s) = t.split(':')
result = int(h) * 3600 + int(m) * 60 + int(s)
