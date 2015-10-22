# How to apply a complex formula using Pandas in Python?
mad = lambda x: np.fabs(x - x.mean()).mean()
rolling_apply(ts, 60, mad).plot(style='k')
