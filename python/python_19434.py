# Reading pdf contents using Python
reading = open('test.txt')
full_paper = reading.read()
split_paper = full_paper.split('Copyright 2014 The New York Times Company. All Rights Reserved.')
