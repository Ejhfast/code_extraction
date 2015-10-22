# How to click links one by one with Selenium webdriver and Python
for i in range(0,6):
    links = browser.find_elements_by_css_selector(MENU_LINKS_CSS_SELECTOR)
    links[i].click()
