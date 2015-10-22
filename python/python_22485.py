# python parse and print text before .(dot)
with open("qwer.txt", 'r') as my_file:
    for line in my_file:
        print line.split('=')[0].split('.')[1]
