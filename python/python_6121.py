# Python removing items from list
people[:] = [p for p in people if p[0] != '' and p[1] != '']
