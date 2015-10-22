# Subtraction of one list of lists from another list of lists
c=[map(lambda x, y: x-y, ii, jj) for ii, jj in zip(a,b)]
