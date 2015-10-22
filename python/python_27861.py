# Subprocess wait expect script to finish
p11 = subprocess.Popen('gnome-terminal -e "perl /tmp/expect',shell=False)
  p11.wait()
