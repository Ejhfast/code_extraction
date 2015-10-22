# Writing a dictionary to a CSV file via DictWriter (Python)
for key, value in dictToSearch.items():
    myWriter.writerow({'md5' : key, 'value': value})
