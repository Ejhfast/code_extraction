# Issue in running system commands from python script continuously?
os.system("screen -d -m /usr/local/sbin/snmpd -f -L -d -p 9999 &amp;")
os.system("screen -d -m python /home/maxuser/utils/python-bg/sock_bg.py &amp;")
