# python: iterating through prefixes
In [9]: [s[:m.start()] for m in re.finditer(':|$', s)]
Out[9]: ['foo', 'foo:bar', 'foo:bar:baz']
