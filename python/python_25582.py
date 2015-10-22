# Find set with range in python
for combo in itertools.product(list1, list2, list3, list4, list5):
    if 27 &lt; sum(list(map(int,combo))) &lt; 31:
        print(combo)
