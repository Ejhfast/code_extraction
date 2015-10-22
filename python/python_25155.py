# Proper way to iterate over a dict value that may or may not be present in Python
for item in a_dict.get("some_key",[]):
    #do whatever
