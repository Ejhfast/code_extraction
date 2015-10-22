# Find a specific tag with BeautifulSoup
soup = BeautifulSoup(htmlstring)
soup.findAll('div', style="width=300px;")
