# How to start a python background process which doesn't block a socket
close() releases the resource associated with a connection but does not necessarily
close the connection immediately. If you want to close the connection in a timely
fashion, call shutdown() before close().
