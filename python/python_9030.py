# Python 2.7, WMI Unexpected COM Error -2147352567 Non-domain system connecting to domain system
def makeConnection(self, parent):
    parent.server = parent.hostlist.pop().strip()
    parent.wmiConnection = wmi.WMI(computer=parent.server, user=parent.username, password=parent.password)
