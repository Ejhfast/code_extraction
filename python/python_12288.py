# Python: Find index of minimum item in list of floats
from operator import itemgetter
min(enumerate(a), key=itemgetter(1))[0]
