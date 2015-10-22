# Iron Python Error: expected <type 'bytes'> or bytearray, got <type 'str'> for Serial comm
ser.write(bytes(message.encode('utf-8')))
