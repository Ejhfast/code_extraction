# Filter out HTML tags and resolve entities in python
import lxml.html
t = lxml.html.fromstring("...")
t.text_content()
