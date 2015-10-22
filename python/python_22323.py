# Python/matplotlib : getting ride of matplotlib.mpl warning
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
