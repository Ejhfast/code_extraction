# How can I get an specific id from html code with python?
inputTag = soup.find(attrs={"name": "stainfo"})
output = inputTag['value']
