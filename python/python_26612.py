# How to crawl 'hidden' JS for locally saved html
fp = webdriver.FirefoxProfile()
fp.set_preference("javascript.enabled", False)
self.driver = webdriver.Firefox(firefox_profile=fp)
