# How to sort a {str:[int]} into a tuple with the string and list of integers based on length of the lists?
s = sorted(data.items(), key=lambda x: x[0])  # alphabetic
s = sorted(s, key=lambda x: len(x[1]), reverse=True)  # length
