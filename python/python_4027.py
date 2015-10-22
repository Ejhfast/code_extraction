# Is there a built-in function to sort and filter a python list in one step?
files = sorted( (f for f in files if firstFile &lt;= int(f) &lt; lastFile), key=int)
