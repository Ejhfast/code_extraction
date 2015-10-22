# Scrapy: parse a div from a list of divs
response.xpath('//li[@class=listclass"]/div[not(contains(@class,"divclass"))]/text()').extract()
