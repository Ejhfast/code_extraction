# Regex help in python
re.search('STATION(?P&lt;StationName&gt;.*?):.*?\n.*?IP Address: %s' % sta_ip, output).group("StationName")
