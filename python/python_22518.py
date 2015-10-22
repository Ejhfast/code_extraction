# writing only dictionary values into a text file
with open('log.txt','w') as log:
    for value in log_disk.values():
        log.write('{}\n'.format(value))
