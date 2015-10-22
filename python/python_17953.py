# swap the first element with the maximum element in the list-Python
index_max = a.index(max(a))
a[index_max], a[0] = a[0], a[index_max]
