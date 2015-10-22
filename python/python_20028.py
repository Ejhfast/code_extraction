# Complex sort dictionary into sorted list
sorted((k, v) for (k, v) in somedict, key=lambda (k, v):
  (-v.dollarsSpent, -(v.itemsPurchased - v.itemsSold),
  -v.itemsPurchased, v.position))
