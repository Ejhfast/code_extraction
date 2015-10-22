# Change values of a python dictionary contigent on the other values of the dictionary
def getHigh(pricedata, start=None, end=None):
    start = min(pricedata) if start is None else start
    end = max(pricedata) if end is None else end
