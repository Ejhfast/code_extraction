# Python Variable Assignment If Variable Exists else None in One Line
data['x'] = locals().get('x','')  # or globals, depending on the scope you need
