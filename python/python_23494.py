# 2D color plot with irregularly spaced samples (matplotlib.mlab.griddata)
# Just include the four corners
X=np.concatenate([np.random.random(100),[0,0,1,1]])
Y=np.concatenate([2*np.random.random(100)-1,[-1,1,1,-1]])
