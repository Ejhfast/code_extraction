# Python a function that counts lines and characters in a file
with open('text.txt') as the_file:
     data = [len(i) for i in the_file]
     line, char = len(data), sum(data)
