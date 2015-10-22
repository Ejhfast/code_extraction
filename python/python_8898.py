# Scrapy and response status code: how to check against it?
class TothegoSitemapHomesSpider(SitemapSpider):
    handle_httpstatus_list = [404]
