# How can I get the href of elements found by partial link text?
links = browser.find_elements_by_partial_link_text('##')
for link in links:
    print link.get_attribute("href")
