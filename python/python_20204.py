# Django - merge two querysets by sorting them
from itertools import chain
 result_list = list(chain(firstq, secondq))
