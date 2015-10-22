# Looking for a more pythonic logical solution
def lone_sum(*args):
      return sum(v for v in args if args.count(v) == 1)
