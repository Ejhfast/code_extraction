# Sending a character to the Arduino serial port using Python's Pyserial
ser = serial.Serial('COM6', 9600)
time.sleep(3)
ser.write('Hello world')
