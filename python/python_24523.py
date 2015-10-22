# Add each preceeding value of a list to the next
mylist = [item + sum(mylist[:index]) for index, item in enumerate(mylist)]
