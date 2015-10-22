# How do I gather user numerical input into a list in Python?
UserNumbers=input("Enter number sequence separated by spaces: ")
nums = [int(i) for i in UserNumbers.split()]
