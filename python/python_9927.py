# Python: Finding max of a dictionaries tupled-value
d = {'one':(1,2,3), 'two':(3,2,1), 'three':(4,5,6)}
tuple(max(x) for x in zip(*d.values()))
