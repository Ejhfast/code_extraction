# Scraping specified links with BeautifulSoup
for link in soup.select("#trendingbox &gt; a"):
    print link.get('href')
