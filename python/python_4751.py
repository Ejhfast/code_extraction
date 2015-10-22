# Matplotlib does not display hatching when rendering to pdf
plt.fill(x,np.sin(x),color='blue',alpha=0.5)
plt.fill(x,np.sin(x),color='None',alpha=0.5,edgecolor='blue',hatch='/')
