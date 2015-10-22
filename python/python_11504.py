# the simple way to check if the elements of a list or set are single type?
type(l[0]) in [int, str] and all( type(e) == type(l[0]) for e in l)
