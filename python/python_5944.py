# xml.parsers.expat.ExpatError on parsing XML
content = requests.get(url = url).content
rss = parse(content).getroot()
