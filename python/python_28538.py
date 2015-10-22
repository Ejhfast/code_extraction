# Web Scraping : Getting HTML source generated from JSP using Python
driver.get(url)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe"))
content = driver.page_source
