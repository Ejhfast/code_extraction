# How do I delete a tuple in a list based on a value in the tuple?
my_table = [elem for elem in my_table if elem[1:] != ('bananas', 1)]
