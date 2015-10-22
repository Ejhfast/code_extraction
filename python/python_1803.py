# Slicing at runtime
def dynSlicing(data, targetsize):
    return data[tuple(slice(x) for x in targetsize)]
