# Scrapy + Change in request parameter
def start_requests(self):
    for i in range(1, 101):
        yield Request(url='http://www.somesite.com/details.html?pageId={0}'.format(i), callback=self.my_callback)
