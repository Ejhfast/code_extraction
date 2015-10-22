# extracting text from noisy string.. python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
soup.find({"class":"fix"})
