# How to call an R function with a dot in its name by pyRserve?
as_integer = getattr(conn.r, 'as.integer')
conn.r.sapply(conn.ref.List, as_integer)
Out[8]: array([1, 2, 3], dtype=int32)
