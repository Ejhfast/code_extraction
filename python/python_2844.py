# Check for presence of a sublist in Python
def sublistExists(list1, list2):
    return ''.join(map(str, list2)) in ''.join(map(str, list1))
