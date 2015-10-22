# How do I read a file line by line and read a list element by element simultaneous in python
for line, item in zip (open ('myfile.txt'), mylist):
  print (line)
  print (item)
