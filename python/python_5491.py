# python: lenient version of iterator.groupby that skips the records on exception
employment = dict(itertools.groupby(xtable_iterator),
                  lambda x: getattr(x, 'key_to_ytable', None))
employment.pop(None)
