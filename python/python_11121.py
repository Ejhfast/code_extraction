# xpath not extracting all fields
doc = LH.fromstring(html)
for td in doc.xpath('//td[not(*)]/text()'):
    print td
