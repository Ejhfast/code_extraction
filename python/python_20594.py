# Why do I need to add DOTALL to python regular expression to match new line in raw string
string = r'\n...\n'
re.search("Subject sentence is:(.*)Causal Verb is :(.*)predicate sentence is:(.*)", string)
