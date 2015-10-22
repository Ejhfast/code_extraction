# How to decode an invalid json string in python
In [1]: import demjson
In [2]: demjson.decode('{ hotel: { id: "123", name: "hotel_name"} }')
Out[2]: {u'hotel': {u'id': u'123', u'name': u'hotel_name'}}
