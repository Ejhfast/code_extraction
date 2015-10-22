# How to run cmd command in Python with admin
import win32com.shell.shell as shell
commands = 'echo hi'
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
