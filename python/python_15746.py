# string.format, differing length breaks table
for i in table_data:
     interface,mac,ip = i
     print '{:&lt;20s}{:&lt;20s}{:&lt;20s}{s}'.format(ip, mac,'ARPA' ,interface)
