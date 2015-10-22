# iterating over dictionary with wildcard key matching
for key in dict
    if re.match(r'npi[0-9]+', key):
        print(dict[key])
