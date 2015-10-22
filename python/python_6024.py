# Python 3.2: How to pass a dictionary into str.format()
stats = { 'copied': 5, 'skipped': 14 }
print( 'Copied: {copied}, Skipped: {skipped}'.format( **stats ) )  #use ** to "unpack" a dictionary
