# 'str' object has no attribute '__dict__'
s = simplejson.dumps([p.__dict__ for p in list.itervalues()])
