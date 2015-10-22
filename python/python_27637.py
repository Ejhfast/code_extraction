# I cannot click the Admin button nested inside the iFrame
WebDriverWait(mydriver, 10).until(lambda d: mydriver.find_element_by_xpath("//div[. = 'Administration']").click())
