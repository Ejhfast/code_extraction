# How to print contents of mongoengine's QuerySet
qs = qs.filter(reduce(operator.or_, or_queries)).as_pymongo()
print qs
