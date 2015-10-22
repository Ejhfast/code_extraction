# Save rpy2.robjects.lib.ggplot2
from rpy2 import robjects
robjects.r.ggsave(filename="x.pdf", plot=p, width=200, height=120, unit='mm')
