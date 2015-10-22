# Running twisted on posix (QNX) system that does not have siginterrupt()
reactor.run(installSignalHandlers=False)
