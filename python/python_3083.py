# Custom sort of directory contents
sorted( ..., key = lambda s: ( not s.startswith( "_" ), s ) )
