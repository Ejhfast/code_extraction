# Feed URL from HTML using Python
import lxml.html
doc = lxml.html.parse(url_to_site)
feeds = doc.xpath('//link[@type="application/rss+xml"]/@href') # list feed urls
