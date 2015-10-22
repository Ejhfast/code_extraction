# Python several variables/functions resutl same line
now  = time.strftime("%X")
peer = socket.getpeername()
print("{} - {}".format(now, peer))
