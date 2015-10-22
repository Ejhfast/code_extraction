# Can anyone help me how to get the value of recursive product using negative input?
def mult(a, b):
    if b&lt;0: return -mult(a, -b)
