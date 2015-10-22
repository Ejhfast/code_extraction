# How can i use scrapy shell to with parameters on url
scrapy shell "http://www.seek.com.au/JobSearch?DateRange=31&amp;SearchFrom=quick&amp;Keywords=python&amp;nation=3000"
&gt;&gt;&gt; from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
&gt;&gt;&gt; lx = SgmlLinkExtractor()
