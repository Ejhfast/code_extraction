# Python Spawn a Thread with Threading and kill when main finishes
thread = threading.Thread(target=MonitorProcess)
thread.daemon = True
thread.start()
