# Passing a list into django model object
for i in list:
    a = Vendas(purchasername=i[0], itemdescription=i[1], itemprice=i[2], purchasecount=i[3], merchantaddress=i[4], merchantname=i[5])
    a.save()
