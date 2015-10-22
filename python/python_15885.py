# Scrapy: How to make a conditional (present or absent) XPATH return values when absent?
xpath = '//li[contains(@class,"our-age")]/span/text()'
item["age"] = hxs.select(xpath).extract() or [' ']
