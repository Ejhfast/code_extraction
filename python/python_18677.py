# Better way to call a chain of functions in python?
out = initial_input
for func in [function1, function2, function3, function4]:
    out = func(out)
