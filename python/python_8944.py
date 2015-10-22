# Python: Read HTML source from URL and get date into program
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(filehandle.read())
titleTag = soup.html.head.title
