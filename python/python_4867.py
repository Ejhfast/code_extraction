# Python code to scan network to obtain the computer name
&gt;&gt;&gt; import _winreg
&gt;&gt;&gt; c = _winreg.ConnectRegistry("SOMEMACHINE", _winreg.HKEY_CLASSES_ROOT)
&gt;&gt;&gt; c = _winreg.ConnectRegistry("10.10.40.9", _winreg.HKEY_CLASSES_ROOT)
