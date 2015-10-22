# Remove number of bytes from beginning of file
f = open('filename.ext', 'rb')
f.seek(255) # skip the first 255 bytes
rest = f.read() # read rest
