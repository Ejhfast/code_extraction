# What is the most pythonic way to avoid specifying the same value in a string
"hello %(name)s , how are you %(name)s, welcome %(name)s" % {"name": "john"}
'hello john, how are you john, welcome john'
