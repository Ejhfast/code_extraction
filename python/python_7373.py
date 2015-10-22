# Selenium - Python - drop-down menu option value
from selenium import webdriver
b = webdriver.Firefox()
b.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()
