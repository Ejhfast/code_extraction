# selenium how to get the content of href within some targeted class
div = self.driver.find_element_by_class_name('someclass')
div.find_element_by_css_selector('a').get_attribute('href')
