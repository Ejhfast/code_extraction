# Python web scraping with regex
battles = soup.find('td', 'td-number-nowidth')
if battles:
   print(battles.get_text())
