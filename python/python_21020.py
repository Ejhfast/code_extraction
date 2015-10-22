# python beautifulsoup iframe document html extract
for iframe in iframexx:
    response = urllib2.urlopen(iframe.attrs['src'])
    iframe_soup = BeautifulSoup(response)
