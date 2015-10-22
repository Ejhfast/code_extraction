# XPath to select an element if previous element contain a matching text() - Python, Scrapy
item['Header_Type']= site.select('div[1]/table[@class="layouttab"]/tr/td[contains(text(),"Type")]/following-sibling::td[1]/text()').extract()
