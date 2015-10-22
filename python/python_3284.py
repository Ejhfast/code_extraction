# Python Sort Two Dimensional Dictionary By First Key
for key1 in sorted(myDict):
    for key2 in myDict[key1]:
        print key1 +"   " +key2 +"   " +myDict[key1][key2]
