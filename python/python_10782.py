# 500 Internal Server Error trying to start session with shopify python api
session = shopify.Session(SHOP_URL)
session.token = PRIVATE_APPLICATION_PASSWORD
shopify.ShopifyResource.activate_session(session)
