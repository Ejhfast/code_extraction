# Python + making a function more generic
ind = something()
for field in ['id', 'name']:
    print getattr(ind, field)
