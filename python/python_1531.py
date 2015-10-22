# How can I support * in user-defined search strings in python?
import re
regex = re.compile('^' + '.*'.join(re.escape(foo) for foo in pattern.split('*')) + '$')
