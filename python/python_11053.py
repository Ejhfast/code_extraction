# How to make all the Handlers(pages) on a google app engine website https
webapp2.Route(r'/products', handler='handlers.ProductsHandler', name='products-list', schemes=['https'])
