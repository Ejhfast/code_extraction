# Efficient User-Agent Regex to find Safari in Python
if 'safari' in userAgentString.lower() and 'chrome' not in userAgentString.lower():
    print "Found Safari"
