# Dynamic file creation(naming)
for idx in range(1,11):
    f = open("POSCAR_%d" % idx, "w")
    f.close()
