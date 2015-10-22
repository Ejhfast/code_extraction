# How can I create a list where if a[0] or a[1] of a row of list a are not present in any rows of list b that row in list a is appended to list c?
for row in a:
    if row[0] not in b or row[1] not in b:
        c.append(a[2])
