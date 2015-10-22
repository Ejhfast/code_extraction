# Perform Task Directly After Returning JSON
t = threading.Thread(target=some_function, args=[argument])
t.setDaemon(False)
t.start()
