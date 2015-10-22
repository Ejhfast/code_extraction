# All nodeValue fields are None when parsing XML
import feedparser
d = feedparser.parse('http://www.digg.com/rss/index.xml')
title = d.channel.title
