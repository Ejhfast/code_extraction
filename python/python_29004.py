# How to get title from class attribute in XPath(Python/scrapy)
item['date'] = sel.xpath('//*[@class="ratingDate relativeDate"]/@title').extract()
item['date'] += sel.xpath('//div[@class="col2of2"]//span[@class="ratingDate"]/text()').extract()
