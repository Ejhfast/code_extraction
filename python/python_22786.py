# Using multiple CSS selectors for the same ArticleItem in Scrapy
article['title'] = response.css("p.title ::text").extract() + \
                   response.css("span.newstitle ::text").extract()
