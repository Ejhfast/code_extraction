# Crawling a site recursively using scrapy
def start_requests(self):
    for i in range(1000):
        yield Request("http://www.example.com/bla-bla-bla/" + str(i), self.parse_tv)
