# Using text(), is there a way to convert empty text to 'None' with scrapy
[txt for item in hxs.select('some-item/value') for txt in item.select('text()').extract() or [u'']]
