# How to solve memory error in mtrand.RandomState.choice?
def item():
    for i in xrange(N):
      yield "id%010d"%np.random.choice(N//K,1)
