# BeautifulSoup - getting value from the resultant tags
average = bookTags.find("span", {"class": "average"})
print average.text
