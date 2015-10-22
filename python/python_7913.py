# Django: Unpack argument list for use in aggregate query
qs = cl.get_query_set()
qs = qs.aggregate(*[Sum(field) for field in tuple])
