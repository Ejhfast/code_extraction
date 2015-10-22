# Is there a pythonic way to update a dictionary value when the update is dependent on the value itself?
def update(dictionary, key, newvalue, func=max):
    dictionary[key] = func(dictionary[key], newvalue)
