# Calculations within pandas aggregate
data = data.groupby(['type', 'name']).agg({'min':np.min, 'max':np.max, 'calculation': calculation})
