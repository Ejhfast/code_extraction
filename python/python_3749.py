# Why does this get a syntax error when exec() is called?
def do_py_validate(field, value):
    exec field.py_validation.replace('\r', '')
