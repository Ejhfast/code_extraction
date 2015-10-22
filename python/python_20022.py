# beautiful soup just get the value inside the tag
volume = soup.findAll("span", {"id": "volume"})[0].string
