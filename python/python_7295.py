# Alternative to eval in Python
import operator
ops = { 'or': operator.or_, 'and': operator.and_ }
print ops[op](True, False)
