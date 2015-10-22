# How to programmatically set a global (module) variable?
definitions = {'a': 1, 'b': 2, 'c': 123.4}
for name, value in definitions.items():
    globals()[name] = value
