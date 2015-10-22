# I failing in storing all the values against a class using selenium web driver
select_boxes = driver.find_elements_by_class_name("action")
for select_box in select_boxes:
    print select_box.get_attribute("value")
