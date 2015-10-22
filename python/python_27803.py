# Ignoring a table's cell class in BeautifulSoup
cols = [ele.text.strip() for ele in cols if ele.get('class',"my default value") != ['quintile', 'detailColumn']]
