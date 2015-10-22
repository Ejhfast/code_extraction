# strip html tags from an xpath @attribute
descriptionHtml = pageopen.xpath('/html/body//div/div/div//div//span/@data-description')
descriptionBody = lxml.html.fromstring(descriptionHtml)
descriptionText = descriptionBody.xpath('text()')
