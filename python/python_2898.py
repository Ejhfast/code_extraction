# How to parse RSS link (get ulr to RSS) from the page in Python framework Scrapy?
qqq = hxs.select("/html/head/link[@type='application/rss+xml']/@href").extract()
