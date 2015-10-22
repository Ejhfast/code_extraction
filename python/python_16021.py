# Python and Selenium find element with non exact name
browser.find_element_by_xpath('//input[contains(@name, "user")]')
browser.find_element_by_xpath('//input[@name="user" or @name="username"]')
