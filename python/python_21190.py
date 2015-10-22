# Beautiful Soup conversion of Unicode characters to HTML entities
from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc)
    print(soup.prettify(formatter="html"))
