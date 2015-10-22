# How can I generate a list of all possible permutations of several letters?
import itertools
for word in itertools.permutations( list_of_letters ):
   print ''.join(word)
