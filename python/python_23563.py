# How to select parent of parent component by xpath
driver.find_element_by_xpath(
    "//*[contains(text(), 'folder name')]/../../..//tr[2]/td[2]/div"
)
