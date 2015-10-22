# DRF test client unable to post list of JSON
response = self.client.post(cart_item_url, data=data, format='json')
