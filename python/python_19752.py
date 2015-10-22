# Iterate a file but taking 5 lines each iteration
for count, myLine in enumerate(myFile):
    t = MyThread(count % 5 + 1, myLine)
    t.start()
