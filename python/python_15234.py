# store multiple integer values in one list and return best value pair
import heapq
heapq.nlargest(10, (k for k in d if d[k][1] &gt; n), key=lambda k: d[k][0])
