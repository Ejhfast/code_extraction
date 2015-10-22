# Accessing yelp API points in Python
for b in response['businesses']:
    print b.get('name', 'missing')
