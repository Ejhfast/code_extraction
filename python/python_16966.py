# print all the values of a group of objects without iterating through it
Products = productBll.listProduct(params)
print [prd.__dict__ for prd in Products]
