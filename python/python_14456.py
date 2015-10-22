# Run a powershell script from python that uses Web-Administration module
subprocess.check_call("c:\\windows\\sysnative\\cmd.exe /c
                       powershell pathToScript", shell=True)
