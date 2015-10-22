# Shorter way of this NumPy list comprehension
# I think it's axis 2, might have to play around there
mask = (im_gray != 255).all(axis=2)
im_out[mask] = im_gray[mask]
