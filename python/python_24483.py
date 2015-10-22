# Take a string and return all occurrences of its first char with a '*'
def asteriskify( string ):
   if len( string ) == 0: return ''   # corner case pointed out by smci
   return string[ 0 ] + string[ 1: ].replace( string[ 0 ], '*' )
