# why will the application show after sys.exit command?
status = app.exec_()   # run app, show window, wait for input
sys.exit(status)       # terminate program with a status code returned from app
