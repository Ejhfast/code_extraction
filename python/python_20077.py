# Extract and merge lists from dictionary
print [v for k in my_dict for v in my_dict[k]]
# ['a', 'b', 'c', 'x', 'y', 'z']
