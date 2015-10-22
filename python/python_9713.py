# extracting specific content from html page
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(your_text)
description = soup.find('a').string
