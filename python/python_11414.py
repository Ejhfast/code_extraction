# how to create a list of lists
list = []
line = np.genfromtxt('temp.txt', usecols=3, dtype=[('floatname','float')], skip_header=1)
list.append(line)
