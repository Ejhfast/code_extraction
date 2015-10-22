# Paging python lists in slices of 4 items
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print [mylist[i:i+4] for i in range(0, len(mylist), 4)]
# Prints [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
