# Turning selected pixels to black based on an HSV hue range
image[np.where((hue2==[0,0,0]).all(axis=2))]=[0,0,0]
