# Block pyhook from so-generated keystrokes?
&gt;&gt;&gt; from ctypes import windll
&gt;&gt;&gt; windll.user32.RegisterHotKey(0, -1, 0x0002, 0x5a)
