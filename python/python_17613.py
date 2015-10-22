# Perform tasks periodically with python irc library
def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        task.LoopingCall(lambda : (self.msg(counterpartID, "hi there"))).start(5.0)
