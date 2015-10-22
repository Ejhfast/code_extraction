# How to parse JSON datetime string in python?
&gt;m = re.search(r"Date\((\d+)\+", 'Date(1354011247940+0000)')
&gt;print(datetime.datetime.fromtimestamp(int(m.group(1))/1000.0).strftime('%Y-%m-%d %H:%M:%S'))
2012-11-27 12:14:07
