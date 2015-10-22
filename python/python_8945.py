# How to get a list of variables in specific Python module?
print [item for item in dir(adfix) if not item.startswith("__")]
