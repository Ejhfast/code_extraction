# Find php string concatenation using python regex
text = "$email = 'hello '.$user1_35.' we would like to annoy you '.$Tod-ay.' for 20 minutes.';"
res = re.findall("'\.(\$[\w-]*)\.'", text)
print res #['$user1_35', '$Tod-ay']
