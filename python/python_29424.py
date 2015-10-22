# convert strings into python dict
import ast
my_dict = ast.literal_eval('{{{0}}}'.format(my_string))
