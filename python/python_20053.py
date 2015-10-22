# How to find element value using Splinter?
xpath = '//p[@class="attrs"]/span[text()="description:"]/following-sibling::strong'
description = browser.find_by_xpath(xpath).first.text
