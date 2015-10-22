# how can i pass a value of variable defined in python to a procedure in mysql as an input?
cursor.execute("call procedure('%s');" % variable )
