# Extracting HTML data fields with Python
from bs4 import BeautifulSoup
soup = BeautifulSoup('&lt;html&gt;&lt;body&gt;&lt;a&gt;bbb&lt;/a&gt;&lt;/body&gt;&lt;/html')
soup.find('a')
