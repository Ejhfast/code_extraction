# Using a sublist to retrieve data from a larger list
searches = ('aa90_273024', 'another_search', 'yet_another_search')
my_result = [item[1:] for item in data if item[0] in searches]
