# BeautifulSoup - findAll not within certain tag
filteredDayContainers = [tag for tag in soup.find_all('div',
    attrs = {'class': 'dayContainer'})
    if "disabled" not in tag.parent['class']]
