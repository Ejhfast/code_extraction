# How do I write "for item in list not in other_list" in one line using Python?
for item in (i for i in my_list if i not in other_list):
    print item
