# Evaluating code after parsing it
from rpy2.robjects.packages import importr
base = importr('base')
base.eval(expr)
