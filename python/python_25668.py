# Dealing with \n delimiter when reading flies in Python
lines = open('the_file.txt').readlines()
lines = [line.strip() for line in lines]
