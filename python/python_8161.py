# What if the utf-8 encoding html file contains a non-utf-8 character?
unicode_html = myfile.read().decode('utf-8', 'ignore')
soup = BeautifulSoup (unicode_html)
