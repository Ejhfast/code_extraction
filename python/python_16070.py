# XML Python Choosing one of numerous attributes using ElementTree
from BeautifulSoup import BeautifulStoneSoup
soup = BeautifulStoneSoup(xml_string)
whatyouwant = soup.find('second-tag')['status']
