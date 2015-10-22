# Selenium WebDriver "find_element_by_xpath" on WebElement
elements = driver.find_elements_by_xpath("//div[@class='Display']")
title = elements[1].find_elements_by_xpath(".//div[@class='Title']")
