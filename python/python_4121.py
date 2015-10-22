# Is there a way to use readability (text extraction algorithm) and a custom algorithm in python to extract links from text?
article = page.summary()   # Extract article using readability
article.findAll("a")       # Return a list of all links in the article
