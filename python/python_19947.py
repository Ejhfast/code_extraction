# How to prevent bleach from escaping > (blockquote) tag used in Markdown
import HTMLParser
h = HTMLParser.HTMLParser()
s = h.unescape(sanitized user input)
