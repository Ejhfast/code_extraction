# Python: Print in rows
food_list = ['apple', 'pear', 'tomato', 'bean', 'carrot', 'grape']
for i in xrange(0, len(food_list), 4):
    print '\t'.join(food_list[i:i+4])
