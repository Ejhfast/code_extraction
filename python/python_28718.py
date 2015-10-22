# In Python, how to format string while saving in a file
with open('test.txt', 'w') as f:
    f.write('{0:10} {1:10}'.format('one', 'two'))
