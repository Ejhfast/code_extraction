# How can I find where a vector value passes a threshold and the n+1 value meets a condition?
locs = (np.diff(np.sign(np.diff(v_1))) &lt; 0).nonzero()[0] +1
