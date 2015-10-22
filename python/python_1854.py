# Reusing module references in Python (Matplotlib)
from matplotlib import mlab
psdResults = mlab.psd(inputData, NFFT=512, Fs=sampleRate, window=blackman)
