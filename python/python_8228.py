# Repeating a python regular expression until a certain char
index = str.find('!')
if index &gt; -1:
    str = str[index:] # or (index+1) to get rid of the '!', too
