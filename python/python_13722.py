# Shopify Python API: How do I add a product to a collection?
collect = shopify.Collect({ 'product_id': product_id, 'collection_id': collection_id })
collect.save()
