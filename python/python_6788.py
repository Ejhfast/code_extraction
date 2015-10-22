# Python: can I modify a Tuple?
for i,(floatnumber_val, prod_id) in enumerate(prodName):
  prodName[i] = (floatnumber_val, prodDict.get(prod_id,prod_id))
