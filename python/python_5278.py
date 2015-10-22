# Python matplotlib contour plot logarithmic color scale
axim    = ax.contourf(X,Y,Z,levels=[1e-3, 1e-2, 1e-1, 1e0],cmap=plt.cm.jet,norm = LogNorm())
