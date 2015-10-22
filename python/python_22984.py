# Renumbering a 1D mesh in Python
lookup_table = dict( zip( old_num, new_num ) ) # create your translation dict
vect_lookup = np.vectorize( lookup_table.get ) # create a function to do the translation
ELEM[:, 1:] = vect_lookup( ELEM[:, 1:] ) # Reassign the elements you want to change
