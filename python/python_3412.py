# Parse a map of int -> list from a string
dict((k, v.split(',')) for k,v in (x.split(':') for x in s.split('::')))
