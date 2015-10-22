# Default parameter in python with objects
def exitDevice(ip,m=None,sendExit=True):
   if m is None: m = getDefaultValueForM()
   if sendExit: m.send ( 'exit' )
