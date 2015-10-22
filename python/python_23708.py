# save RData workspace in Python using rpy2
from rpy2.robjects.packages import importr
base = importr('base')
base.save_image(&lt;arguments here...&gt;)
