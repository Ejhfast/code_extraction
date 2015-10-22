# How to filter list of dictionaries with matching values for a given key
def copyf(dictlist, key, valuelist):
      return [dictio for dictio in dictlist if dictio[key] in valuelist]
