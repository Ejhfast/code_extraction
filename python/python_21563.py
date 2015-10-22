# python : scrapy using proxy IP
DOWNLOADER_MIDDLEWARES = {
 #you need this line in order to scrap through a proxy/proxy list
'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
