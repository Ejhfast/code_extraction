# substring in python
s = "2011-03-01 14:10:43 C:\Scan\raisoax.exe detected    Trojan.Win32.VBKrypt.agqw"
reg = re.match(r"\S*\s\S*\s(.*)[^\ ] detected\s+(.*)",s)
file,name = reg.groups()
