# how to find the correlation between two images
from scipy import signal
cor = signal.correlate2d (im1, im2)
