# Taking the total number of lines from a file reading process
fileinput = open('tweets.txt', 'r')
lines = [line.lower() for line in fileinput]
