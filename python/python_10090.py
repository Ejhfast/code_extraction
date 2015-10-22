# Python creating a list with itertools.product?
new_list = [item for item in itertools.product(*start_list) if sum(item) == 200]
