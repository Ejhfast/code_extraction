# Using re.sub() in python to replace html code
print re.sub(r"(&lt;table)",r"\1 border=1",test_Str)
