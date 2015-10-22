# Python raw_input doesn't work after using subprocess module
def execute(command):
    return subprocess.check_call('plink.exe -ssh ' + USER + '@' + HOST + ' -pw ' + PASSWD + ' ' + command, stdin=open(os.devnull))
