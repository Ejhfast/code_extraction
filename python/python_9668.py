# Some website content causes BeautifulSoup (and lxml) to restart Python session
page=urllib2.urlopen('http://www.nasa.gov/').read().replace("&lt;!DOCTYPE \"xmlns:xsl='http://www.w3.org/1999/XSL/Transform'\"&gt;", "&lt;!DOCTYPE html&gt;")
