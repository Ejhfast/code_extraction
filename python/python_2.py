# How do I download a file over HTTP using Python?
import urllib2
response = urllib2.urlopen('http://www.example.com/')
html = response.read()
