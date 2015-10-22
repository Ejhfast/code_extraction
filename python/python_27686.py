# list comprehension with tuple comparision
inp = [("abc", 1, "def"), ("abc", 1, "ghi"), ("bc", 2, "a"), ("bc", 2, "b"), ("bc", 3, "a")]
res = []
[res.append(el) for el in inp if not [tmp for tmp in res if tmp[0] == el[0] and tmp[1] == el[1]]]
