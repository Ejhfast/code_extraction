# Python and HTML table
food_list = ['car', 'plane', 'van', 'boat', 'ship', 'jet','shuttle']
for i in xrange(0, len(food_list), 4):
    print '&lt;tr&gt;&lt;td&gt;' + '&lt;/td&gt;&lt;td&gt;'.join(food_list[i:i+4]) + '&lt;/td&gt;&lt;/tr&gt;'
