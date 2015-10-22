# Efficient way to do these python list comprehensions
self.newList, self.timeStamp = zip(*((x.rstrip(), '0') for i, x in enumerate(rawFile) if i%2==0))
