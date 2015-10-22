# django - import different module when variable change
module_name = 'a.foo'
module = __import__(module_name, globals(), locals(), ['*'])
