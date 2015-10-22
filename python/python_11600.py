# two level sorting of a list of dictionaries in python
sorted(mylist, key=lambda d: (d["id"], -d["score"]))
