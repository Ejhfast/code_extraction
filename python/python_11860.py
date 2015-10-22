# appending to the strings within a list of strings in python
first_list = ['foo','bar','baz']
second_list = [x+y for x,y in zip(first_list,'dsy')]
