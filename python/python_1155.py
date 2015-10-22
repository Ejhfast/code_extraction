# Python list filtering and transformation
In [5]: versions = [m.group(1) for m in [regex.match(lib) for lib in libs] if m]
In [6]: versions
Out[6]: ['3.3.1', '3.2.0']
