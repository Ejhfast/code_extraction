# Generating a PNG with matplotlib when DISPLAY is undefined
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
