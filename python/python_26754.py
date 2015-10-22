# How can I extract data from a html tag using Python?
soup = bs4.BeautifulSoup(html)
q1=soup.find('li', class_="sense_list_item level_1",value='1').text
