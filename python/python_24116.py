# Plot linear model in 3d with Matplotlib
exog = pd.core.frame.DataFrame({'TV':xx.ravel(),'Radio':yy.ravel()})
out = fit.predict(exog=exog)
ax.plot_surface(xx, yy, out.reshape(xx.shape), color='None')
