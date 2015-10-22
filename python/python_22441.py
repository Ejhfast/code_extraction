# Turn off interactive mode in FTP
session.retrbinary(("RETR " + f), open(f, 'wb').write)
