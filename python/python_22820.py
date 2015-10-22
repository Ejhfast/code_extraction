# Select reference level in y-variable/ LHS/ endogenous side using patsy
import statsmodels.api as sm
dta = sm.datasets.get_rdataset('iris', cache=True)
