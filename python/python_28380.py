# Django view: Convert unicode retrieved from db to string
import ast
 str_diag_val =ast.literal_eval(diag_val)
 print "diag value=", str_diag_val[0], " ", str_diag_val[1]
