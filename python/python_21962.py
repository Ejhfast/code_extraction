# uwsgi: Can't stop a Flask app
t = Thread(target=print_queue_size, args=())
t.setDaemon(True) # Does the trick
t.start()
