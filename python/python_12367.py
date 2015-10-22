# How to refer to the whole array within reduce()?
result = (lambda array: reduce(lambda a,b: some_function(b,array), array))(original_array[:])
