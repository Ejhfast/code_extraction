# numpy loadtxt single line/row as list
a,b,c = loadtxt("data.dat", usecols(0,1,2), unpack=True)
 a,b,c = (a,b,c) if usi.shape else ([a], [b], [c])
