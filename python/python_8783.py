# Building a regular expression to match the first of multiple occurrences in Python
re.search("&lt;([^&gt;]*)", the_string).group(1)
