# Deploying matlab app on the web using python
command = "mymatlabprogram.exe %s"%(arg1,)
process = subprocess.Popen(command.split())
stdout, stderr = process.communicate()
