# How can I convert this string to list of lists?
str = "[[0,0,0],[0,0,1],[1,1,0]]"
strs = str.replace('[','').split('],')
lists = [map(int, s.replace(']','').split(',')) for s in strs]
