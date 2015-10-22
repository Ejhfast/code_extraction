# print lists in a file in a special format in python
with open('somefile.txt', 'w') as fp:
  for i, s in enumerate(X):
    print &gt;&gt;fp, '%d. %s' % (i + 1, ' '.join(s))
