# Adding RMS noise to an image
from scipy import stats
my_noise=stats.distributions.norm.rvs(0,2,size=your_array.shape)
your_array+=my_noise
