# positions in a list. python
for i, sublist in enumerate(lst):
    for j, elem in enumerate(sublist):
        sublist[j] = 3*(i+1)*(j+1)
