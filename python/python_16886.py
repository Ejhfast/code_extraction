# More elegant way to create a list of lines from BeautifulSoup.findAll
data_to_parse = BeautifulSoup(html_payload)
for line in data_to_parse.get_text().split("\n"):
    pass  # ... do something
