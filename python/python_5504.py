# Simple string match
def matchStr(ipadr = '10.20.30.40', matchIP = '10.20.'):
    return ipadr.startswith(matchIP)
