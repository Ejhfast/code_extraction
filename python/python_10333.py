# Tkinter can't work while a socket loop is happening
t = Thread(target=start_server)
t.start()
