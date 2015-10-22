# Is there a way to use readability and python to extract just text, not HTML?
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
text =  soup.get_text()
