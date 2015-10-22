# How to remove brackets from JSON in Python?
result = {"MetaData": {}, "SRData": dResult}
print(json.dumps(result, sort_keys=True, indent=4))
