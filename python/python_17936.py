# How to clear surface
sf = ax.plot_surface(x,y,z,rstride=5,cstride=5,color='r',linewidth=0.1,shade=0) # - this function
sf.remove()
