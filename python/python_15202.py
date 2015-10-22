# Python / Scipy - implementing optimize.curve_fit 's sigma into optimize.leastsq
popt, pcov, infodict, errmsg, ier = curve_fit(func, xdata, ydata, sigma = SD, full_output = True)
