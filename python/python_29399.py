# Python : How to search for values in a table outside an if function?
utilisateur2 = next((u for u in list if u.nom == utilisateur.arg), None)
if utilisateur2 == None:
   # not found
