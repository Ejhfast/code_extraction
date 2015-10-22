# Python _winreg - read REG_BINARY
import subprocess
cmd = ['C:\Windows\sysnative\cmd.exe /c REG QUERY HKLM\LocationToBinaryValue /v' BinaryValueName']
subprocess_checkoutput(cmd, shell=True)
