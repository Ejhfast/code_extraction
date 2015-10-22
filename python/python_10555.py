# Scaled colormap of facecolors with mplot3d
ax.plot_surface(X,Y,z, facecolors=plt.cm.jet(np.clip(fc,0,vmax)*np.max(z)/vmax), cstride=1, rstride=1, vmax=vmax)
