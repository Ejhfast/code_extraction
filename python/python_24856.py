# Simplify statement '.'.join( string.split('.')[0:3] )
version = '1.2.3.4.5-RC4'                 # the end can vary a lot
api = '.'.join(version.split('.')[0:3])   # extract '1.2.3'
