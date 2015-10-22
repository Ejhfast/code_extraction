# Clean Up HTML in Python
from BeautifulSoup import BeautifulSoup
tree = BeautifulSoup(bad_html)
good_html = tree.prettify()
