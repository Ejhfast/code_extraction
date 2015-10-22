# How to get a JS redirected pdf linked from a web page
souppage = BeautifulSoup(p.text)
 line = souppage.findAll('a',text=re.compile("requested"))[0]
 pdf = requests.get(ofstedbase+line['href'])
