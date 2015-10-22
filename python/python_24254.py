# Parse json file with ironpython 2.5
jsonstring = open('myfile.json').read()
data = eval(jsonstring)
