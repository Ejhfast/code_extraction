# Python Find distance between two coordinates
def diff256(a, b):
  return min((a - b) % 256, (b - a) % 256)
