# Extract URL where text matches a regex - with XPath 1.0
.select('//a[. != "" and translate(., "0123456789", "") = ""]/@href')
