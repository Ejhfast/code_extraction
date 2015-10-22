# Extract opengraph, twitter, and fb meta data from html
mdata = []               # if you prefer 1-liners, use a list comprehension
for md in soup.find_all('meta'):
    mdata.append(md)
