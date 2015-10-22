# Is there an elegant way to cycle through a list N times via iteration (like itertools.cycle but limit the cycles)?
import itertools
itertools.chain.from_iterable(itertools.repeat([1, 2, 3], 5))
