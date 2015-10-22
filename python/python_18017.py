# Scrapy Crawler - How do I specify which links to crawl
rules = (
        Rule(SgmlLinkExtractor(allow=('http://www.cseblog.com/{d+}/{d+}/{*}.html', ), deny=( )),call_back ='parse_save' ),
        Rule(SgmlLinkExtractor(allow=('http://www.cseblog.com/search/{*}', ), deny=( )),,call_back = 'parse_only' ))
