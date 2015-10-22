# Mechanize - Add to form post submission
self.browser.form.new_control('text','options[5]',{'value':''})
self.browser.form.fixup()
self.browser["options[5]"] = "New option."
