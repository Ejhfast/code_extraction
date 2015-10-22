# FTP upload files Python
ftp.storlines("STOR " + filename, open(filename, 'r'))
