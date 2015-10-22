# Printing net-snmp getbulk results with newlines at each index
result = session.getbulk(0, 48, vars)
for i in range(0, len(result), 3):
    print "ifind: "+result[i]+" ifdesc: "+result[i+1]+" status: "+result[i+2]
