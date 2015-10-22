# How to access comments using lxml
from lxml.html import HtmlComment # or similar
no_comments=[element for element in element_list if not isinstance(element, HtmlComment)]
