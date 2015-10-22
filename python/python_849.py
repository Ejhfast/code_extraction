# How to open a file and find the longest length of a line and then print it out
print max(open(your_filename, 'r'), key=len)
