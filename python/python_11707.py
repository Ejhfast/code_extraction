# Set Windows command-line terminal title in Python
&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.windll.kernel32.SetConsoleTitleA("My New Title")
