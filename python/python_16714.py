# python german umlaut issues - 'ascii' codec can't decode byte 0xe4 in position 15: ordinal not in range(128)
uname =  ("'" + row[2]+"'").decode('utf-8') # Just that you need
