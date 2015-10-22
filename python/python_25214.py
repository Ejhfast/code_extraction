# Pattern to resolve mongoDB references
resolved_products = list(mycollection.find({'_id': {'$in': result['products']}}))
