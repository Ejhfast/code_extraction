# Scrapy grab div with multiple classes?
from scrapy import Selector
sel = Selector(text='&lt;div class="product product-small"&gt;I am a product!&lt;/div&gt;')
print sel.css('.product').extract()
