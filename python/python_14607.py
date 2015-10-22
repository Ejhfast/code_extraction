# Sorting one list to match another in python
object_map = {o['id']: o for o in objects}
objects = [object_map[id] for id in ids]
