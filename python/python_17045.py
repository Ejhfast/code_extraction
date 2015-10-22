# Piping commands in plink on windows command line
ff=subprocess.Popen("plink root@server -pw pass rpm -qa",shell=False,stdin=subprocess.PIPE)
ff.communicate("grep string &gt; rpm.txt")
