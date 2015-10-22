# display current process stdout in PySide QTextEdit box
sys.stdout.close()
sys.stdout = open("out.txt", "w")
