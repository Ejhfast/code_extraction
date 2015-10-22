# Listing serial ports in Mac OS X and Python 3
&gt;&gt;&gt; import glob
&gt;&gt;&gt; glob.glob('/dev/tty.*')
['/dev/tty.Bluetooth-Incoming-Port', '/dev/tty.Bluetooth-Modem']
