# What is the use of Python's basic optimizations mode? (`python -O`)
def foo(x):
    assert x in huge_global_computation_to_check_all_possible_x_values()
    # ok, go ahead and use x...
