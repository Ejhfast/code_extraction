# Submitting a post request to an aspx page
browser= mechanize.Browser()
    browser.select_form(form_name)
    browser.set_value("Page$Next", name="pagenumber")
