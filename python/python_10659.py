# R fitdistr for Beta distribution: which starting parameters?
from rpy2.robjects import DataFrame
starter= DataFrame({'shape1':0.5,'shape2':0.5})
x = MASS.fitdistr(myValues, "beta", start=starter))
