# use dictionary_1's keys to search for a match in dictionary_2's values
list1 = [ key for key in mydict1.keys() if key in mydict2.itervalues() ]
