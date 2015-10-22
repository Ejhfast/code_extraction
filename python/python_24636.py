# Scrape elements inside tag properties - Scrapy
hxs.select('//embed[@id='flash-player-embed']/@flashvars').extract()[0].split('url_bigthumb=')[1].split('key')[0].replace('&amp;amp;','').strip().replace('&amp;','').strip()
