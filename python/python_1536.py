# os.listdir etc fails on shared windows path (Python 2.5)
def toUnix(path):
    return path.replace("\\", "/")
