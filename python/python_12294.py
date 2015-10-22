# How to split multiline string to array
from bs4 import BeautifulSoup
parser = BeautifulSoup(remote_data)
link_list = [a['href'] for a in parser.find_all('a')]
