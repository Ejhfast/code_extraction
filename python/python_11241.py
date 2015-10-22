# Correct way to transform python request parameters
result = simplejson.loads(request.params.get('abc', '{}'))
