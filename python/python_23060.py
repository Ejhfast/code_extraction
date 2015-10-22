# re.match one from a set of strings, with result as variable
In [2]: re.match(r'(test2|test3|test)','test2').group(1)
Out[2]: 'test2'
