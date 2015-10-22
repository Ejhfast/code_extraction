# Python server chat issue when run
while True:
    client, addr = sock.accept()
    Thread(target=clientHandler, args=(client, addr)).start()
