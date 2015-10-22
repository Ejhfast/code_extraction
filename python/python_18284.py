# Locating specific <p> tag after <h1> tag in Python Html Parser
&gt;&gt;&gt; page_txt = urllib2.urlopen("http://b-line.binghamton.edu/events/9305").read(
&gt;&gt;&gt; soup = bs4.BeautifulSoup(pg.split("&lt;h1&gt;",1)[-1])
&gt;&gt;&gt; print soup.find_all("p")[:3]
