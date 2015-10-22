# how do I display the elements in the slice all on one line separated by a single space and sorted in highest to lowest order
def process(total):
    total.sort()
    return total[1:-1] #take all numbers except the first and the last
