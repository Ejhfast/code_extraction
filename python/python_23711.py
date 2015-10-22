# Grab what is after f1= but ignore \r\n and \n if they are present
a = re.search(r'(?&lt;=f1=)(.*)', a.strip())
