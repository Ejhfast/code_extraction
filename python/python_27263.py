# Using Scrapy to crawl a list of urls in a section of the start url
rules = (Rule(LinkExtractor(restrict_xpaths=(".//*[@id='mw-content- text']/ul[19]"), ), callback='parse_items', follow=True),
 Rule(LinkExtractor(deny_domains='...start url...'), callback='parse_items',follow= True),)
