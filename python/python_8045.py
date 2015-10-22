# Processing HTML files Python
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup('Your resource&lt;title&gt;hi&lt;/title&gt;')
soup.title.string # Your title string.
