# How should one manage hook specific files in the '.hg/' state directory?
f = self.wopener("mydata", "w", atomictemp=True)
f.write(somedata)
f.close()
