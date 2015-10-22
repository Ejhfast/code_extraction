# How to remove extra stuff at front and end of html fetched via xpath
response.xpath('//*[@id="example"]/textarea/text()').extract()[0].strip()
