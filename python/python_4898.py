# Problems with regex matching
for tag in soup.findAll('a', href = re.compile('^/l[0-9]+/.*$')):
    print tag['href']
