# loop over 2 lists, repeating the shortest until end of longest
result = ["_".join((i, j)) for i, j in itertools.izip(la, itertools.cycle(lb))]
