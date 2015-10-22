# Crawlspider not scraping anything
rules = [Rule(SgmlLinkExtractor(allow = ('/\d+.htm')), follow=True,
    callback='parse_item'),]
