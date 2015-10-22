# How to remove the 2nd element of every tuple in a list of 3-ples?
my_list = [tuple([j.split()[0] for j in i]) for i in my_list]
