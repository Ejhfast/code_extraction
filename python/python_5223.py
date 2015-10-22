# Python string length recursion
def recursiveLength(theString):
    if theString == '': return 0
    return 1 + recursiveLength(theString[1:])
