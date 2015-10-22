# Scrapy Follow & Scrape next Pages
rules = ( Rule(LinkExtractor(allow=('course-finder', ),restrict_xpaths=('//div[@class="pagination"]',)), callback='parse_items',follow=True), )
