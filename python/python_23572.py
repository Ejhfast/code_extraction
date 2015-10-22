# Scrapy/Python/XPath - How to extract data from within data?
for t in response.xpath('//*[@id="categories"]/ul'):
    for x in t.xpath('.//li'):
