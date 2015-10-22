# Searching on class names with a dash ('-')
from cssselect import HTMLTranslator
result = lxml_document.xpath(HTMLTranslator().css_to_xpath('div.reddit-entry'))
