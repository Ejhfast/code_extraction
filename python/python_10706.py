# Changing string dictionary values into integers and adding them up
for k, v in my_dict.items():
    my_dict[k] = str(sum(int(c) for c in v))
