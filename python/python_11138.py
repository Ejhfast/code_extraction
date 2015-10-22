# Python-How to add a struct.pack value to an integer that would be sent through the serial port
POS_SERVO = struct.pack('&lt;h', int(posicion))
