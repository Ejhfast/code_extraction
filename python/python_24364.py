# Scrapy Extract number from page text with regex
response.xpath('string(//body)').re(r"Units: (\d)")
