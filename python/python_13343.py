# How can I check if a checkbox is checked in Selenium Python Webdriver?
def is_checked(self, driver, item):
  checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
  return checked
