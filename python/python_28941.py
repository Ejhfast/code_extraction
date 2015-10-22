# How to find string in item of list python
cities = [w.split(',')[0] for w in my_list]
term = "de"
results = [city for city in cities if term in city.lower()]
