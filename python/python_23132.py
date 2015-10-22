# AttributeError: 'str' object has no attribute 'string'
myRawInput = raw_input("Enter some numbers separated by spaces")
myList = myRawInput.split()
myList.sort()
