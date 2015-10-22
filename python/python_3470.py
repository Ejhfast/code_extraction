# python serval variables combine into a dict?
def debug_info ( self ):
    for ( key, value ) in self.__dict__.items():
        print( key, '=', value )
