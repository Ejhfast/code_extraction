# python string conversion for eval
import re
exp = 'qty * price - discount + 100'
exp = re.sub('(qty|price|discount)','%(\\1)f', exp)%vars(obj)
