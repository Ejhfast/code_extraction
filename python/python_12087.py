# Plotting graphs with several lines rpython2 - additional lines won't show
from rpy2.robjects.vectors import IntVector
r.lines(x, IntVector(y) - 500, col = "green")
