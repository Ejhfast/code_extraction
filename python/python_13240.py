# Scrapy - 2 classes - Blank Item-FIelds
item['price'] = prei.select("td[@class='ticket_price td-cell ucase black strong align-right']/text()").extract()
if len(item['price']) == 0:
   item['price'] = prei.select("td[@class='ticket_price td-cell ucase black strong align-right row-border']/text()").extract()
