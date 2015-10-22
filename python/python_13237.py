# Remove spike noise from data in Python
import scipy.ndimage as im
x= im.median_filter(x, (self.m,self.m))
