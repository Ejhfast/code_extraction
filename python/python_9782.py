# Creating instances in a loop with different variables
list_of_names = ['a', 'b', 'c', 'd']
for name in list_of_names:
    globals()[name] = your_object()
