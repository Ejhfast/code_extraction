# How to use output processor in ItemLoader from Scrapy to sort a list?
def process_item(self, item, spider):
    return sorted(item['body'])
