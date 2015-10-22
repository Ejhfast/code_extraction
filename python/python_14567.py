# Is there a more pythonic way to loop over multiple similar indices using list comprehension?
from itertools import product
A = [(X(x), Y(y), Z(z)) for x, y, z in product(range(N), repeat=3)]
