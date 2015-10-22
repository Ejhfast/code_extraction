# capturing states between tags in python using xpath
word = tree.xpath('//div[@class="message2"]/strong/text()')[0]
sentence = tree.xpath('//div[@class="message2"]/strong/following-sibling::text()[1]')[0]
