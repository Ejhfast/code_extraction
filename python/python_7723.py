# Scrapy read list of URLs from file to scrape?
f = open("urls.txt")
start_urls = [url.strip() for url in f.readlines()]
f.close()
