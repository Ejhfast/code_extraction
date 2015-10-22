# Python and Tar command shell=True
date = str(now.year)+str(now.month)+str(now.day)
filename = date + "backup_lucas.tar.gz"
subprocess.Popen(['tar', '-pczf', filename, '/home/lucas/backup/'])
