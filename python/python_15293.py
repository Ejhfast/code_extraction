# A simple regexp in python
input_user2 = re.sub(r'MM\(([^\)]*)\)', r"MM('\1')", input_user)
 output = re.sub(r'func\(([^,]*),', r"func('\1',", input_user)
