# Getting specific data with BeautifulSoup
soup = BeautifulSoup(""" &lt;div class="item"&gt; &lt;b&gt; name &lt;/b&gt;  &lt;br/&gt;  stuff here &lt;/div&gt;""")
soup.find("div", "item").find('br').nextSibling
