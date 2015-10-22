# mongodb elemMatch in dual array
db.cart.find_one({'cart': {'$elemMatch': { '$elemMatch' : {'id': 1, 'count': {'$gt': 2}}}}})
