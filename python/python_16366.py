# CrawlSpider get source link when crawling
def mycallback(self, response):
        print "Referer:", response.request.headers.get("Referer")
        ...
