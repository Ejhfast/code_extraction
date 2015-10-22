# Using python scrapy to extract links from a webpage
rules = [
         Rule(LinkExtractor(allow='boxscores/\w+'), callback='parse_item')
]
