# Is there any way to access <option> text when parsing forms using lxml.html?
options = doc.xpath("//select[@name='country']/option")
option_text = [option.text for option in options]
