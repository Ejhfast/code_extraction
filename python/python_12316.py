# Extract URLs with lxml
urls = tree.xpath('//div[@class="pics"]/a/@href') +
       tree.xpath('//div[@class="name"]/a/@href')
