# Python - bulk promote variables to parent scope
globals().update(__import__(sys.argv[1]).__dict__)
