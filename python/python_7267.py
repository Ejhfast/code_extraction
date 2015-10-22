# How to chain a ssh, cd, then execution in subprocess.Popen
subprocess.Popen('ssh root@IP "cd /opt/msys/pe2/bin;./perlscript.pl;" -a file.csv'
