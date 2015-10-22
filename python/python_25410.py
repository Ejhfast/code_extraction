# split string according to words between square parenthesis
x="[python] how to [css]"
print re.findall(r"(?&lt;=\[)[^\]]*(?=\])",x)   # this is the list you want
print re.sub(r"\[[^\]]*\]","",x)             # this is the string you want
