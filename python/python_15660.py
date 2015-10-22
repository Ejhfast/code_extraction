# "Backspace" over last character written to file
f.seek(-1, os.SEEK_CURR)
f.write(";")
