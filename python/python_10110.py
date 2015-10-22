# How do I create a list of all occurances of a string which ends with a specific file type found in a text file?
re.findall('"([^"]*\.(?:gif|jpg)[^"]*)"', text)
