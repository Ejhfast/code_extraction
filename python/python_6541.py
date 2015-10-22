# Why is Paramiko raising EOFError() when the SFTP object is stored in a dictionary?
t = paramiko.Transport((host, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
