# Nothing returned when using 32 bit Python os.popen on a 64 Bit Windows 7 System
import os
os.popen(r'C:\Windows\SysNative\manage-bde.exe -status c:').read()
