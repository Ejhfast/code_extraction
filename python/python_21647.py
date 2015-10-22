# Select element whose child/grandchildren/.. contains an element with a specified pattern
e = doc.xpath('//tr[td[text()="Welcome"]]')[0]
