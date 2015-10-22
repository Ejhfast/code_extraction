# scrapy, I am trying to remove empty lines that are extracted to a csv file
if not (item['url'] == "" and item['model'] == "" and item['year'] == ""):
    items.append(item)
