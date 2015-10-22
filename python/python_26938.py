# Simplifying a nested for loop with comprehension
rooms = set([r for resort in otas.values() for room in resort.values() for r in room])
