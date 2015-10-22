# use beautiful soup to parse a href from given html structure
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
print [a["href"] for a in soup.select('h3.r a')]
