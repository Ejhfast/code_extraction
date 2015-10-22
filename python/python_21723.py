# Scipy curve_fit does not seem to change the initial parameters
p0 = [np.max(y_points), x_points[np.argmax(y_points)], 0.1]
coeff, var_matrix = curve_fit(gaussFunction, x_points, y_points, p0)
