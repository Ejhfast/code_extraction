# How can I replace text inside the parentheses using re.sub()
In [3]: import re
In [4]: re.sub("\([^)]*","(x",'(1) item 1. \n(2) item 2')
Out[4]: '(x) item 1. \n(x) item 2'
