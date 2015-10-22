# Python Web Scraping W/O Beautiful Soup or non-default modules?
import urllib2,re
content = urllib2.urlopen("http://somme.url").read()
print re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",content)
