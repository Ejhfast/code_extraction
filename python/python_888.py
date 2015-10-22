# Delete None values from Python dict
result = default.copy()
result.update((k, v) for k, v in user.iteritems() if v is not None)
