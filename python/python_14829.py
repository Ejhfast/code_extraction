# Permutations, iterator, recursion and double loop
for item, other_items in pick_item(items):
        yield from _permutations_rec(current+item, other_items, n)
