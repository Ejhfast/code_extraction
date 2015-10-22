# Alter XPath to Extract Text Selenium
element = browser.find_elements_by_css_selector('.tl-cell.tl-popularity')
text = element.get_attribute('data-tooltip')
