# Scrapy: re-crawling with the same rule
Rule(SgmlLinkExtractor(allow=("ShowUserReviews-g.*",), restrict_xpaths=('//*[@id="REVIEWS"]/div[4]/div/div[2]/div/div/div[1]/a[text() = "Next"]',), unique=True), callback='parse_item', follow= True)
