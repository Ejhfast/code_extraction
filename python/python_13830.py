# xml split because of junk python
xml = xml.split('&lt;/response&gt;', 1)[0] + '&lt;/response&gt;'
