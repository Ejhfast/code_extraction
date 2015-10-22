# How to read telnet sessions with python
tn = telnetlib.Telnet('localhost', 10011, 10)
tn.read_some()
