# find if background image is used for any html tag with inline style
doc.xpath('//*[contains(@style,"background") and contains(@style,"url(")]')
