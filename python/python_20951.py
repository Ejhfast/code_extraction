# Only Allow Internal Links in Broad Scrapy Web Crawl
domain = response.url.replace("http://","").replace("https://","").split("/")[0]
links = [k for k in links if domain in k.url]
