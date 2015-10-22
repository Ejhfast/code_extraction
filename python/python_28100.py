# Using more than one flag in python re.findall
x = re.findall(r'CAT.+?END','Cat \n eND',re.I | re.DOTALL)
