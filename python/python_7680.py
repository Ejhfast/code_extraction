# In Python - Selenium2 how to set the time for which a webdriver instance should wait,when loading a page,before giving a timeout exception?
WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))
