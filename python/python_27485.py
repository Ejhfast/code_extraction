# Python: Pass 1 argument to a 2d array of functions and get results in 2d array of same size
N_gsi = lambda gsi: [ [1/4*(1+gsi[1]), 1/4*(1+gsi[0])], [-1/4*(1+gsi[1]), 1/4*(1-gsi[0])], [-1/4*(1-gsi[1]), -1/4*(1-gsi[0])], [1/4*(1-gsi[1]), -1/4*(1+gsi[0])]]
