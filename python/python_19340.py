# Applying a decorator to a property getter
prop = property(memoized(prop.fget), prop.fset, prop.fdel, prop.__doc__)
