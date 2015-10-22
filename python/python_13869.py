# MySQL Query interfaceerror
Intermittent errors could occur on Windows systems: InterfaceError(errno=2013).
The cause was incorrect handling of sock.recv() library calls that returned less
data than was requested. (Bug #14829471, Bug #67303)
