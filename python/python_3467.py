# Python variables as keys to dict
for i in ('apple', 'banana', 'carrot'):
    fruitdict[i] = locals()[i]
