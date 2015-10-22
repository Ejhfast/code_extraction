# Using optparse to read in a list from command line options
import ast
(options, args) = parser.parse_args()
myopt = ast.literal_eval(options.myopt)
