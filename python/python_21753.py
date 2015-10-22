# plt.axis(): How to 'tight' axis hiding boundary NaNs?
x = np.arange(0,a.shape[1])
plt.xlim([x[~np.isnan(a[0,:])][0],x[~np.isnan(a[0,:])][-1]])
