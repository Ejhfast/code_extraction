# Assigning an argument to a global variable with the same name
my_var = 1
def my_function(my_var):
    globals()['my_var'] = my_var
