# Plot numpy datetime64 with matplotlib
from datetime import datetime
a=np.datetime64('2002-06-28').astype(datetime)
plot_date(a,2)
