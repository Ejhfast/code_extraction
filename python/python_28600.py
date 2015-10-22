# How to reverse key value pair in list with dictionary as value?
l = ((1,{'foo':1,'abc':2,'xyz':3,'def':2}),(2,{'ghu':3,'kie':2}))
tuple((({k:v}),i) for i,j in l for k,v in j.items())
