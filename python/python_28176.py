# python regular expression with re.split()
x="400-IF(3&gt;5,5,5)+34+IF(4&gt;5,5,6)"
print [i for i in re.split(r"IF\([^)]*\)",x) if i]
