# Using json with list of lists. How to append lists in loop in file and later load it as list of lists
with open('database.txt','a+') as myfile:
    json.dump(lst, myfile)
    myfile.write('\n')
