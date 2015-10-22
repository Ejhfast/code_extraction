# scipy: Interpolating trajectory
from scipy import interpolate
tck,u=interpolate.splprep([x,y],s=0.0)
x_i,y_i= interpolate.splev(np.linspace(0,1,100),tck)
