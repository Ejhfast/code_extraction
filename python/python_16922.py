# Group query results in batches of Python
total = Message.objects.all().count()
for i in xrange(0,total,500):
   batch = Message.objects.all()[i:500]
