# Why is this code so CPU and memory intensive?
q = MyModel.all(keys_only=True)
for i in xrange(0, 1000, 200):
    db.delete(q.fetch(200))
