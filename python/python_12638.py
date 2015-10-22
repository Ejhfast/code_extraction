# How can I find specific but obscure elements in Selenium, without a parser like Beautiful Soup?
browser.find_elements_by_xpath(
    "//span[contains(text(), 'secs') or contains(text(), 'mins') or contains(text(), 'hrs')]")
