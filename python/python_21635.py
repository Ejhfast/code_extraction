# Wrong encoding when displaying an HTML Request in Python
parser = HTMLParser.HTMLParser
parsed = parser.unescape(r.text)
