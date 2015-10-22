# How to list only top level directories in Python?
&gt;&gt;&gt; [ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]
['ctypes', 'distutils', 'encodings', 'lib-tk', 'config', 'idlelib', 'xml', 'bsddb', 'hotshot', 'logging', 'doc', 'test', 'compiler', 'curses', 'site-packages', 'email', 'sqlite3', 'lib-dynload', 'wsgiref', 'plat-linux2', 'plat-mac']
