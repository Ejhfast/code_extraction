# python how to put argument to function with numpy aply_along_axis
def my_function_allong_axis(M, argument):
    return np.apply_along_axis(my_function, 0, M, argument)
