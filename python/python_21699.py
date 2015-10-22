# Handle pagination in python scrapy
start_urls = ['http://www.example.com/s/ref=lp_1805560031_pg_4?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031&amp;page={0}&amp;ie=UTF8&amp;qid=1400668237'.format(page) for page in xrange(1,30)]
