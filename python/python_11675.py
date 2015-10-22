# How to write a python script for downloading?
f = open(localFilePath, 'w')
f.write(urlopen(remoteFilePath).read())
f.close()
