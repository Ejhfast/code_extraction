# Scrapyd: Writing CSV file to remote server
curl http://amazonaws.com:6800/schedule.json -d project=wallspider -d spider=cppages -d setting=FEED_URI=/home/ubuntu/scrapy/sitemapcrawl/results/cppages.csv -d setting=FEED_FORMAT=csv -d setting=JOBDIR=/home/ubuntu/scrapy/sitemapcrawl/crawl/cppages-nov
