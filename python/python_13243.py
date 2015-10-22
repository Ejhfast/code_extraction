# Reading a Unit Test to a file in python with a custom function
logFile = open("C:/folder/logfile.txt", "w")
unittest.TextTestRunner(stream=logFile, verbosity=2).run(customFunction())
logFile.close()
