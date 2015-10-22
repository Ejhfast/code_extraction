# Truncating all the elements(floats) in a numpy.ndarray
center_a = center.tolist()   # Convert numpy array into list
center_b = center_1.tolist() # Convert numpy array into list
np.allclose(center_b,center_a,rtol=1e-04, atol=1e-04)
