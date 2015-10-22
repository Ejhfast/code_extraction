# How to run an xpath over html page in python?
import lxml.html
page = lxml.html.parse('http://www.google.com').getroot()
print page.xpath('//a/@href')
