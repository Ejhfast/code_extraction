# Python - Beautiful Soup - Remove Tags
numbers_data = [int(e.text) for e in soup.find_all('td', 'right')]
