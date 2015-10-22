# Scipy Leastsq Optional Output Variable (Mesg)
import scipy.optimize as optimize
p,cov,infodict,mesg,ier = optimize.leastsq(
    residuals,p_guess,args=(x,y),full_output=True)
