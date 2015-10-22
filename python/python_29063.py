# How to use Beautiful Soup's find() instead of find_all() for better runtime
line = soup.find('img', attrs={'data-a-dynamic-image': True})
