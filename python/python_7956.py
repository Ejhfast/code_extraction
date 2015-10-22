# python, tailer and logrotate
for line in tailer.follow(open('test.txt')):
    print line
