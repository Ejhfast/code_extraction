# Python thread starts running before calling Thread.start
t1=threading.Thread(target=self.read)
t1.start()
print "something"
