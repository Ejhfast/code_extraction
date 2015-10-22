# How can I get a suitable representation of levels in pandas.cut?
import pandas as pd
x = pd.cut(np.arange(0,20), 10)
np.array(map(lambda t:t[1:-1].split(","), x.levels), float)
