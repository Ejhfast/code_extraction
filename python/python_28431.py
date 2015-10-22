# Iterate Two Ranges In For Loop
import itertools as it
for i in it.chain(range(30, 52), range(1, 18)):
    print(i)
