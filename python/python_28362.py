# Detecting first 20 chars in string in mark_safe()
z="12345678 912345678 15235213523 23512351235"
print re.sub(r"^(.{20})",r"\1&amp;nbsp;",z,flags=re.UNICODE)
