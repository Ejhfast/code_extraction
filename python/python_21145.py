# how can i do math operation on list elements in python?
nums = [3,51,34]
reduce(lambda x, y: [y] if not x else x + [y + x[-1]], nums, None)
# [3, 54, 88]
