# How can I retrieve the page title of a webpage using Python?
import lxml.html
t = lxml.html.parse(url)
print t.find(".//title").text
