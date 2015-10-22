# In python using Regex, how do I insert a string after a string with a close-parenthesis character?
re.sub(r"(\):[0-9\.]+)",r"\1 " + string, line1)
