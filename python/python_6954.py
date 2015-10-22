# Avoid a Newline at End of File - Python
fileout = open('out.txt', 'w')
list = ['a', 'b', 'c', 'd']
fileout.write('\n'.join(list))
