# simple string concatenation in python for wrapping shell scripts
proc = Popen([\"ifconfig\",\"" +first_interface+ "\",\"192.168.100.1\"], stdout=PIPE)\n\
