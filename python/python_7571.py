# create new string by adding characters of smaller strings one after another
result = ''.join(map(''.join, zip(*strings)))
