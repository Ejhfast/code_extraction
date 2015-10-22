# Extract a dictionary from <key><val>...<key><val> wiredata
tiddata = '&lt;Mkey3&gt;&lt;456&gt;&lt;Mkey2&gt;&lt;Mval2&gt;&lt;MKey1&gt;&lt;MVal1&gt;'
t = tiddata.strip('&lt;&gt;').split('&gt;&lt;')
output = {t[i]: t[i+1] for i in range(0, len(t), 2)}
