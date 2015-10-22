# How to sort list of objects
List.sort(key=lambda e: [e.a, e.b, e.c])
# or
List.sort(key=operator.attrgetter('a', 'b', 'c'))
