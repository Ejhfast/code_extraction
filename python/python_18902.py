# Add variable in HtmlXPathSelector select function
sel.select('//a[contains(@href, "{0}")]/@href'.format(url_type)).extract()
