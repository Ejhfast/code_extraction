# I have a galaxy image and I only want to plot the 500th row
plt.imshow(data2[499].reshape(1,-1),interpolation="none",cmap="binary")
