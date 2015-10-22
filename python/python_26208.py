# NumPy analog of R's `filter`
import numpy, scipy.signal
taps = numpy.repeat(1.0/9, 9)
smoothed_x = scipy.signal.lfilter(taps, 1.0, x)
