# How to call from within Python an application with double quotes around an argument using subprocess?
output=subprocess.Popen(("certutil.exe -view -restrict  \"NotAfter&lt;=now+30:00,NotAfter&gt;=now+00:00\"" ),stdout=subprocess.PIPE).stdout
