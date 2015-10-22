# How can I call a DLL from a scripting language?
&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; windll.user32.MessageBoxA(None, "Hello world", "ctypes", 0);
