# What's the best possible way to do this kind of dict matching in python?
for key in ['value', 'value_1', 'value_2']:
    report[key] = data.get(key, None) # or just data.get(key), since None is the default
