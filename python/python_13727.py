# Create a list of tuples from list in python
[(tag.text, urlparse.urljoin(url, tag['href']))
        for tag in soup.findAll('a', href=True)]
