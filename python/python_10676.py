# How to download a file via FTP with Python ftplib
ftp.retrbinary('RETR %s' % filename, file.write)
