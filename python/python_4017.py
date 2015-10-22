# How do I download a website using python 3?
from urllib.request import urlopen
html = urlopen("http://www.stackoverflow.com/").read().decode('utf-8')
print(html)
