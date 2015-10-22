# In Python, how do I make a datetime that is 15 minutes from now? 1 hour from now?
d1 = datetime.datetime.now() + datetime.timedelta(minutes=15)
d2 = datetime.datetime.now() + datetime.timedelta(hours=1)
