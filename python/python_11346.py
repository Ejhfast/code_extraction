# using variables in attributes using xpath & scrapy
for x in range(100):
    str_selector = '/tr[@name="tag_{0}"]/td/text()'.format(x)
    hxs.select(str_selector)
