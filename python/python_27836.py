# Trying to scrap data from a website dicksmith.com.au
reg = re.compile('\?w=mobile\+phone&amp;ts=m')
rules = [ Rule ( LinkExtractor(allow = reg, 'parse_dickSmith' ) ]
