# Can someone convert this python to list comprehension?
processed = [[val if not isinstance(val,basestring) else str(val) for val in row] for row in schema]
